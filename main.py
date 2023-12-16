import time
import random
import os
import matplotlib.pyplot as plt

sizes = [10, 100, 1000, 10000, 100000, 1000000]
def generate_word():
    word = ""
    number_of_letters = random.randint(1, 10)
    for _ in range(number_of_letters):
        letter_ascii = random.randint(97, 122)
        word += chr(letter_ascii)
    return word + " "


def generate_line():
    line = ""
    number_of_words = random.randint(1, 20)
    for _ in range(number_of_words):
        line += generate_word()
    return line + " "


def generate_paragraph(number_of_lines):
    paragraph = ""
    for _ in range(number_of_lines):
        paragraph += generate_line() + "\n"
    return paragraph


def generate_text():
    with open('data.txt', 'w') as file:
        for size in sizes:
            file.write(str(size))
            file.write("\n")
            file.write(generate_paragraph(size))


def creation_de_text_dans_un_fichier():
    try:
        if os.path.exists("data.txt") == 0 or os.stat("data.txt").st_size == 0:
            generate_text()
        else:
            print("the file is not empty")
    except:
        print("An exception occurred file doesnt exist")


def calculate_number_of_occurrences(word):
    times = []
    number_of_repetitions = 1
    with open('data.txt', 'r') as file:
        current_position = 0
        for size in sizes:
            count = 0
            result = 0
            for _ in range(number_of_repetitions):
                file.seek(current_position)  # Set file pointer to the previous position
                lines = file.readlines()[current_position + 1:size + 1]  # Read only the relevant lines
                # Get the current position after reading lines
                start = time.time()
                for line in lines:
                    words = line.split()
                    for j in words:
                        if j == word:
                            count += 1
                end = time.time()
                result += end - start
            average_times = result / number_of_repetitions
            times.append(average_times)
            current_position = size + 1

            print(f"For size {size}, occurrences of the word '{word}': {count}")
            print(f"It takes an average of {average_times} seconds to search for the word\n")

    return times


def traçage_courbe():
    creation_de_text_dans_un_fichier()
    word_to_search = generate_word()
    search_times = calculate_number_of_occurrences(word_to_search)
    plt.plot(sizes, search_times, label="The Search of Number of Occurences Time")
    plt.xlabel("Size")
    plt.ylabel("Average Time (seconds)")
    plt.title(f"Time for search the number of occurence for word '{word_to_search}'")
    plt.legend()
    plt.show()


traçage_courbe()
