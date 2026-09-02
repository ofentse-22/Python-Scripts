"""Practical 01: Variables and assignment.

Topics from the notes:
- Creating variables
- Variable naming rules
- Case sensitivity
- Assignment operators
- Global and local variables
"""

course_name = "Python Fundamentals"
student_count = 12
average_mark = 76.5
is_beginner_class = True

# Python variables are case sensitive.
student = "Anele"
Student = "Beverly"
STUDENT = "Chris"

# Good variable names start with a letter or underscore and contain no spaces.
total_score = 0
_temporary_value = 25

# Invalid examples. These stay as comments because they would stop the file.
# 2students = 10
# total score = 100
# if = "keyword"

global_message = "I was created outside the function."


def show_global_message():
    """A function can read a global variable."""
    print(global_message)


def show_local_message():
    """A variable created inside a function is local to that function."""
    local_message = "I only exist inside this function."
    print(local_message)


def update_score():
    score = 10
    print("Starting score:", score)

    score += 5
    print("After score += 5:", score)

    score -= 3
    print("After score -= 3:", score)

    score *= 2
    print("After score *= 2:", score)

    score /= 4
    print("After score /= 4:", score)


def main():
    print("Course:", course_name)
    print("Students:", student_count)
    print("Average mark:", average_mark)
    print("Beginner class:", is_beginner_class)
    print()

    print("Case-sensitive names:")
    print("student =", student)
    print("Student =", Student)
    print("STUDENT =", STUDENT)
    print()

    show_global_message()
    show_local_message()
    print()

    update_score()


if __name__ == "__main__":
    main()
