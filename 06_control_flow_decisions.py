"""Practical 06: Control flow with decisions.

Topics from the notes:
- if
- elif
- else
- Nested if statements
"""


def classify_age(age):
    if age >= 18:
        return "You are an adult."
    elif age <= 2:
        return "You are a baby."
    else:
        return "You are a minor."


def describe_number(number):
    if number <= 20:
        if number % 2 == 0:
            return "It is an even number and less than or equal to 20."
        else:
            return "It is an odd number and less than or equal to 20."
    else:
        return "It is greater than 20."


def grade_mark(mark):
    if mark >= 80:
        return "Distinction"
    elif mark >= 70:
        return "Excellent"
    elif mark >= 50:
        return "Passed"
    else:
        return "Not yet competent"


def main():
    ages = [1, 15, 20]
    for age in ages:
        print("Age", age, ":", classify_age(age))

    print()
    for number in [15, 16, 25]:
        print("Number", number, ":", describe_number(number))

    print()
    for mark in [45, 65, 75, 90]:
        print("Mark", mark, ":", grade_mark(mark))


if __name__ == "__main__":
    main()
