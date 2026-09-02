"""Practical 02: Strings.

Topics from the notes:
- Quotes and escape characters
- Multi-line and raw strings
- Immutability
- Concatenation and repetition
- Formatting
- Comparisons
- String methods
"""


def show_quotes():
    single_quote = 'Apple'
    double_quote = "Apple"
    quote_inside = 'This is a "great" apple.'
    escaped_quote = "This is a \"great\" apple."

    print(single_quote)
    print(double_quote)
    print(quote_inside)
    print(escaped_quote)


def show_multiline_and_raw_strings():
    poem = """Hello World!
This string uses more than one line.
Python keeps the line breaks."""

    windows_path = r"C:\mypc\Desktop"

    print(poem)
    print("Raw path:", windows_path)
    print("Escape character example: first line\nsecond line")


def show_string_immutability():
    word = "python"
    print("Original word:", word)
    print("Uppercase copy:", word.upper())
    print("Original word is still:", word)

    # Strings cannot be changed in place.
    # word[0] = "P" would cause a TypeError.
    word = "P" + word[1:]
    print("New string:", word)


def show_concatenation_and_repetition():
    name = "Rich"
    surname = "De Billot"
    full_name = name + " " + surname

    print("Full name:", full_name)
    print("Repeated word:", "Python " * 3)
    print("Today is " + "Saturday")


def show_formatting():
    day = "Saturday"
    season = "winter"
    print("Today is {0}. I like {1}.".format(day, season))

    shopping_list = [
        ("Coffee", 2.00),
        ("Cake", 5.00),
        ("Milk", 1.75),
    ]

    print()
    print("{0:^20}".format("Shopping List"))
    print("{0:<10} | {1:>7}".format("Item", "Cost"))
    print("-" * 20)

    total = 0
    for item, cost in shopping_list:
        total += cost
        print("{0:<10} | R{1:>6.2f}".format(item, cost))

    print("-" * 20)
    print("{0:<10} | R{1:>6.2f}".format("Total", total))


def show_comparisons():
    print("'apple' == 'apple':", "apple" == "apple")
    print("'apple' != 'banana':", "apple" != "banana")
    print("'apple' < 'banana':", "apple" < "banana")

    first = "hello"
    second = "hello"
    print("Use == for same value:", first == second)
    print("Use is only for same object:", first is second)


def show_string_methods():
    sentence = "   this is a great day   "
    messy = "aaa orange aa"

    print("Upper:", sentence.upper())
    print("Lower:", sentence.lower())
    print("Strip:", sentence.strip())
    print("Left strip:", sentence.lstrip())
    print("Right strip:", sentence.rstrip())
    print("Strip a:", messy.strip("a"))
    print("'123'.isdigit():", "123".isdigit())
    print("'12a'.isdigit():", "12a".isdigit())

    message = "this is a great day"
    print("Find 'day':", message.find("day"))
    print("Find 'is':", message.find("is"))
    print("Split:", message.split(" "))


def main():
    show_quotes()
    print()
    show_multiline_and_raw_strings()
    print()
    show_string_immutability()
    print()
    show_concatenation_and_repetition()
    print()
    show_formatting()
    print()
    show_comparisons()
    print()
    show_string_methods()


if __name__ == "__main__":
    main()
