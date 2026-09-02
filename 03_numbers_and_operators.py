"""Practical 03: Numbers and operators.

Topics from the notes:
- Integers
- Floats
- Arithmetic operators
- Floor division and modulo
- Operator precedence
"""


def show_number_types():
    apples = 5
    price = 2.50
    large_number = 12345678901234567890

    print("Integer:", apples, type(apples))
    print("Float:", price, type(price))
    print("Large integer:", large_number)


def show_arithmetic():
    a = 10
    b = 3

    print("a =", a)
    print("b =", b)
    print("Add:", a + b)
    print("Subtract:", a - b)
    print("Multiply:", a * b)
    print("Divide:", a / b)
    print("Exponent:", a ** b)
    print("Floor divide:", a // b)
    print("Modulo remainder:", a % b)


def show_precedence():
    result_without_parentheses = 2 + 3 * 4
    result_with_parentheses = (2 + 3) * 4

    print("2 + 3 * 4 =", result_without_parentheses)
    print("(2 + 3) * 4 =", result_with_parentheses)

    full_example = (10 + 2) ** 2 / 4
    print("(10 + 2) ** 2 / 4 =", full_example)


def show_practical_calculator():
    item_cost = 15.99
    quantity = 4
    discount = 10

    subtotal = item_cost * quantity
    discount_amount = subtotal * discount / 100
    total = subtotal - discount_amount

    print("Subtotal: R{0:.2f}".format(subtotal))
    print("Discount: R{0:.2f}".format(discount_amount))
    print("Total: R{0:.2f}".format(total))


def main():
    show_number_types()
    print()
    show_arithmetic()
    print()
    show_precedence()
    print()
    show_practical_calculator()


if __name__ == "__main__":
    main()
