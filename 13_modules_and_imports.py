"""Practical 13: Modules and imports.

Topics from the notes:
- import package_name
- package_name.function_name()
- from module import function
- help()
- math, datetime, sys, os.path, random
- Building and importing your own module
"""

import datetime
import math
import os.path
import random
import sys
from math import sqrt

import student_math_tools


def show_math_module():
    print("math.sqrt(25):", math.sqrt(25))
    print("sqrt(36):", sqrt(36))
    print("math.pi:", math.pi)


def show_datetime_module():
    today = datetime.datetime.now()
    print("Current date and time:", today)
    print("Year:", today.year)
    print("Month:", today.month)
    print("Day:", today.day)


def show_sys_module():
    print("Python executable:", sys.executable)
    print("Number of command-line items:", len(sys.argv))


def show_os_path_module():
    file_name = "abc.txt"
    print("Does abc.txt exist?", os.path.isfile(file_name))


def show_random_module():
    print("Random number from 1 to 10:", random.randint(1, 10))
    print("Random choice:", random.choice(["red", "green", "blue"]))


def show_own_module():
    print("student_math_tools.add(5, 10):", student_math_tools.add(5, 10))
    print("student_math_tools.subtract(10, 3):", student_math_tools.subtract(10, 3))
    print("student_math_tools.square(4):", student_math_tools.square(4))
    print("student_math_tools.is_even(8):", student_math_tools.is_even(8))
    print("student_math_tools.factorial(5):", student_math_tools.factorial(5))


def main():
    show_math_module()
    print()
    show_datetime_module()
    print()
    show_sys_module()
    print()
    show_os_path_module()
    print()
    show_random_module()
    print()
    show_own_module()


if __name__ == "__main__":
    main()
