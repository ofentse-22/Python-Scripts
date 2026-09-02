"""Small helper module for the modules practical."""


def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def square(number):
    return number ** 2


def is_even(number):
    return number % 2 == 0


def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    answer = 1
    for value in range(1, number + 1):
        answer *= value

    return answer
