"""Practical 10: Command-line arguments.

Topics from the notes:
- import sys
- sys.argv
- Arguments arrive as strings
- Converting arguments to numbers

Try:
py "Python Fundamentals notes\\10_command_line_arguments.py" 5 10
py "Python Fundamentals notes\\10_command_line_arguments.py" Scott Thomas
"""

import sys


def get_arguments():
    arguments = sys.argv[1:]

    if len(arguments) >= 2:
        return arguments[0], arguments[1]

    print("No two command-line arguments were supplied.")
    print("Using default examples: 5 and 10")
    return "5", "10"


def add_as_strings(first, second):
    return first + second


def add_as_integers(first, second):
    return int(first) + int(second)


def main():
    first, second = get_arguments()

    print("First argument:", first)
    print("Second argument:", second)
    print("As strings:", add_as_strings(first, second))

    if first.isdigit() and second.isdigit():
        print("As integers:", add_as_integers(first, second))
    else:
        print("These arguments cannot both be converted to integers.")


if __name__ == "__main__":
    main()
