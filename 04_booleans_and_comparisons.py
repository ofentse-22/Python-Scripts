"""Practical 04: Booleans and comparisons.

Topics from the notes:
- True and False
- Comparison operators
- and, or, not
- Boolean values for numbers and strings
"""


def show_comparisons():
    age = 20

    print("age == 20:", age == 20)
    print("age > 18:", age > 18)
    print("age >= 18:", age >= 18)
    print("age < 18:", age < 18)
    print("age <= 18:", age <= 18)
    print("age != 18:", age != 18)


def show_logical_operators():
    has_id = True
    is_adult = True
    is_vip = False

    print("Adult and has ID:", is_adult and has_id)
    print("Adult or VIP:", is_adult or is_vip)
    print("Not VIP:", not is_vip)


def show_truth_tables():
    values = [True, False]

    print("AND table")
    for left in values:
        for right in values:
            print(left, "and", right, "=", left and right)

    print()
    print("OR table")
    for left in values:
        for right in values:
            print(left, "or", right, "=", left or right)


def show_bool_conversion():
    print("bool(10):", bool(10))
    print("bool(0):", bool(0))
    print("bool('Python'):", bool("Python"))
    print("bool(''):", bool(""))
    print("True + True:", True + True)
    print("True + False:", True + False)


def main():
    show_comparisons()
    print()
    show_logical_operators()
    print()
    show_truth_tables()
    print()
    show_bool_conversion()


if __name__ == "__main__":
    main()
