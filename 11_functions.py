"""Practical 11: Functions.

Topics from the notes:
- Defining functions
- Calling functions
- Parameters
- Optional parameters
- Keyword arguments
- return
- Docstrings
- Built-in conversion functions
- Functions and methods
"""


def add(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def print_addition(first_number, second_number):
    answer = first_number + second_number
    print(answer)


def greet(first_name, last_name="!"):
    if last_name == "!":
        return "Hello " + first_name + last_name

    return "Hello " + first_name + " " + last_name + "!"


def show_conversions():
    print("str(10):", str(10))
    print("int('10'):", int("10"))
    print("float('10.5'):", float("10.5"))
    print("bool('Python'):", bool("Python"))

    user_value = "student input"
    print("input() example value:", user_value)

    # eval() can execute Python code. Use it only with trusted strings.
    print("eval('4 + 5'):", eval("4 + 5"))
    print("eval('4 + 5 / 2'):", eval("4 + 5 / 2"))


def show_function_and_method_difference():
    fruit = "apple"

    print("Function example: len(fruit) =", len(fruit))
    print("Method example: fruit.upper() =", fruit.upper())
    print("Lower:", fruit.lower())
    print("Swapcase:", fruit.swapcase())
    print("Capitalize:", fruit.capitalize())
    print("Format:", "I like {}".format(fruit))
    print("Strip:", "   apple   ".strip())
    print("Right strip:", "   apple   ".rstrip())
    print("Left strip:", "   apple   ".lstrip())


def main():
    print("Calling a function that prints:")
    print_addition(3, 4)
    print_addition(5, 10)
    print()

    print("Calling a function that returns:")
    result = add(1, 2)
    print(result)
    print("Docstring:", add.__doc__)
    print()

    print(greet("John", "Doe"))
    print(greet("John"))
    print(greet(last_name="Dou", first_name="John"))
    print()

    show_conversions()
    print()
    show_function_and_method_difference()


if __name__ == "__main__":
    main()
