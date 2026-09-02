"""Practical 12: Troubleshooting and error handling.

Topics from the notes:
- Syntax errors
- Runtime errors
- Logic errors
- try
- except
- else
- finally
"""


def divide_numbers(first_number, second_number):
    try:
        answer = first_number / second_number
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    else:
        print("Answer:", answer)
    finally:
        print("Division example complete.")


def read_missing_file():
    try:
        with open("missing_file.txt", "r", encoding="utf-8") as file_object:
            print(file_object.read())
    except FileNotFoundError:
        print("The file could not be loaded.")


def get_list_item(items, index):
    try:
        print("Item:", items[index])
    except IndexError:
        print("That index does not exist in the list.")


def show_logic_error():
    mark = 75

    wrong_result = mark > 80
    correct_result = mark >= 50

    print("Wrong pass check:", wrong_result)
    print("Correct pass check:", correct_result)


def main():
    divide_numbers(5, 0)
    print()
    divide_numbers(10, 2)
    print()
    read_missing_file()
    print()
    get_list_item(["red", "green", "blue"], 10)
    print()
    show_logic_error()


if __name__ == "__main__":
    main()
