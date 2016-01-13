#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""
Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
"""
add things in dictionary with word as a key
and number of times that word appeared as a value in that key.
convert words to lowercase and then store in dictionary
"""
def get_dict(filename):
    """
    :param filename:
    :rtype:dict of words as key and number of times that word(Lowercase+uppercase)
            appeared in that text file as value
    """
    word_file = open(filename, 'rU')
    dictionary = {}
    for line in word_file:
        words = line.split()
        for word in words:
            if word.lower() not in dictionary:
                # i made a silly mistake and that was looking for keys in both cases and
                # storing keys in lowercase so overwriting my keys and that was bad and sad :-(
                dictionary[word.lower()] = 1
            else:
                dictionary[word.lower()] += 1
    word_file.close()
    return dictionary
"""
Define print_words(filename) and print_top(filename) functions.
You could write a helper utility function that reads a file
and builds and returns a word/count dict for it.
Then print_words() and print_top() can just call the utility function.
"""
def print_words(filename):
    word_dict = get_dict(filename)
    # print word in sorted alphabetical manner
    for word in sorted(word_dict.keys()):
        print(word, word_dict[word])    # prints word and it's times it appeared in file

def get_tuple(word_dict_tuple):
    # used while custom sorting
    # because dict. stores key:value in a tuple we are accessing last value aka count of word in our case
    return word_dict_tuple[1]

def print_top(filename):
    # print top 20 used word
    dict_word = get_dict(filename)
    items = sorted(dict_word.items(), key=get_tuple, reverse=True)

    for item in items[:20]:
        print(item[0], item[1])  # print key and value form item tuple that we got form items list of tuples

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.

def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
    main()
