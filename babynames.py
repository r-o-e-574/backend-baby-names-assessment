#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""
# give credits
__author__ = "Ruben Espino and I got help from Paul Racisz and Chris Warren"

import sys
import re
import argparse


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    year = filename[4:8]
    names_dict = {}
    with open(filename, 'r') as textfile:
        matches = re.findall(
            r"<td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>", "\n".join(textfile))
        #loop over list of tuples
        for match in matches:
            #i[0] is equal to the rank
            #i[1] is the boy name
            #i[2] is the girl name
            if match[1] not in names_dict:
                #puts in dict as key value pair
                names_dict[match[1]] = match[0]
            if match[2] not in names_dict:
                names_dict[match[2]] = match[0]
        names_sorted_list = sorted(names_dict.keys())
        names = [year]
        for key in names_sorted_list:
            names.append(key + " " + names_dict[key])
            
    return names


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    # For each filename, call `extract_names()` with that single file.
    # Format the resulting list as a vertical list (separated by newline \n).
    # Use the create_summary flag to decide whether to print the list
    # or to write the list to a summary file (e.g. `baby1990.html.summary`).
    for file_name in file_list:
        get_names = extract_names(file_name)
        get_names = "\n".join(get_names)
        if not create_summary:
            print(get_names)
        else:
            new_file = file_name + ".summary"
            files = open(new_file, 'w')
            files.write(str(get_names))

if __name__ == '__main__':
    main(sys.argv[1:])
