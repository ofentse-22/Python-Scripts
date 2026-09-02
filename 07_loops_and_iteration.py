"""Practical 07: Loops and iteration.

Topics from the notes:
- for loops
- range()
- while loops
- factorial
- break
- continue
- pass
- loop else
"""


def loop_through_list():
    fruits = ["apple", "banana", "orange"]

    for fruit in fruits:
        print(fruit)


def loop_with_range():
    print("Numbers from 0 to 9")
    for number in range(10):
        print(number)

    print("Numbers from 10 to 19")
    for number in range(10, 20):
        print(number)

    print("Every second number from 10 to 18")
    for number in range(10, 20, 2):
        print(number)


def repeat_message():
    for _ in range(10):
        print("Hello world!")


def factorial(number):
    answer = 1

    for value in range(1, number + 1):
        answer = answer * value

    return answer


def while_loop_count():
    number = 1

    while number <= 10:
        print(number)
        number += 1


def show_break():
    for number in range(1, 10):
        if number == 5:
            print("Stopping at 5")
            break
        print(number)


def show_continue():
    print("Odd numbers from 1 to 19")
    for number in range(1, 20):
        if number % 2 == 0:
            continue
        print(number)


def show_pass():
    for number in range(1, 6):
        if number == 3:
            pass
        else:
            print(number)


def show_loop_else():
    search_for = "pear"
    fruits = ["apple", "banana", "orange"]

    for fruit in fruits:
        if fruit == search_for:
            print("Found", search_for)
            break
    else:
        print(search_for, "was not found.")


def main():
    loop_through_list()
    print()
    loop_with_range()
    print()
    repeat_message()
    print()
    print("5! =", factorial(5))
    print()
    while_loop_count()
    print()
    show_break()
    print()
    show_continue()
    print()
    show_pass()
    print()
    show_loop_else()


if __name__ == "__main__":
    main()
