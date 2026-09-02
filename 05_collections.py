"""Practical 05: Collections.

Topics from the notes:
- Lists
- Tuples
- Dictionaries
- Sets
- Collection comparison table
"""


def show_lists():
    fruits = ["apple", "banana", "orange"]
    more_fruits = ["peach", "pear"]

    print("First fruit:", fruits[0])
    print("Combined list:", fruits + more_fruits)

    fruits.append("pineapple")
    print("After append:", fruits)

    fruits.extend(["grape", "mango"])
    print("After extend:", fruits)

    fruits.remove("banana")
    print("After remove:", fruits)

    fruits.insert(0, "kiwi")
    print("After insert:", fruits)

    print("Index of orange:", fruits.index("orange"))
    print("Length:", len(fruits))

    numbers = [5, 10, 2, 8]
    print("Numbers:", numbers)
    print("Minimum:", min(numbers))
    print("Maximum:", max(numbers))
    print("Sum:", sum(numbers))
    print("Slice [0:3]:", numbers[0:3])
    print("Every second item:", numbers[0:4:2])


def show_tuples():
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    print("Tuple:", days)
    print("First day:", days[0])

    days_as_list = list(days)
    days_as_list.append("Saturday")
    updated_days = tuple(days_as_list)
    print("Converted and updated:", updated_days)


def show_dictionaries():
    student = {
        "name": "Thabo",
        "course": "Python",
        "mark": 82,
    }

    print("Name:", student["name"])

    student["status"] = "Passed"
    print("After adding status:", student)

    student["mark"] = 88
    print("After updating mark:", student)

    del student["course"]
    print("After deleting course:", student)


def show_sets():
    languages = {"Python", "Java", "Python", "C#"}
    print("Set removes duplicates:", languages)

    languages.add("JavaScript")
    print("After add:", languages)

    print("Is Python in the set?", "Python" in languages)


def show_collection_table():
    comparison = [
        ("List", "Yes", "Yes", "Yes"),
        ("Tuple", "Yes", "No", "Yes"),
        ("Dictionary", "Yes", "Yes", "No duplicate keys"),
        ("Set", "No", "No", "No"),
    ]

    print("{0:<12} {1:<10} {2:<12} {3}".format(
        "Collection", "Ordered", "Changeable", "Duplicates"
    ))
    print("-" * 50)
    for name, ordered, changeable, duplicate in comparison:
        print("{0:<12} {1:<10} {2:<12} {3}".format(
            name, ordered, changeable, duplicate
        ))


def main():
    show_lists()
    print()
    show_tuples()
    print()
    show_dictionaries()
    print()
    show_sets()
    print()
    show_collection_table()


if __name__ == "__main__":
    main()
