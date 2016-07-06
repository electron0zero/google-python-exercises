#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""
Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>

m = re.search(r'[0-9][0-9][0-9][0-9]', s)

>>> m.group(0)
'1990'
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    :param filename: name of html file from which we get data
    :return: returns a list starting with the year string
    followed by the name-rank strings in alphabetical order
    """
    file = open(filename, 'r')
    for line in file:
        # extract year from file
        searchobj = re.search(r'Popularity in [0-9][0-9][0-9][0-9]', line)
        if searchobj:  # if there is a search object then print it
            match = searchobj.group()
            year = match.split()
            print(year[-1:])    # prints the year of which file is inputted

        # extract name and rank from file
        # searchobj = re.search(r'', line)


    return


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    # print(args)
    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
    # print(args);
    # +++your code here+++
    # for loop with if condition to take care of each file
    # and decide what to with file output based on summary file flag
    # dummy for test
    # TODO
    # this is a hack to test name regex
    extract_names(args[0]);


if __name__ == '__main__':
    main()
