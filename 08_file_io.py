"""Practical 08: File input and output.

Topics from the notes:
- Opening files
- Reading and writing
- Closing files
- File modes
- read(), readlines(), seek(), tell()
- The with keyword
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
GENERATED_DIR = BASE_DIR / "generated_files"


def write_file():
    GENERATED_DIR.mkdir(exist_ok=True)
    file_path = GENERATED_DIR / "myfirstfile.txt"

    file_object = open(file_path, "w", encoding="utf-8")
    characters_written = file_object.write(
        "first line\nsecond line\nthird line\n"
    )
    print("Characters written:", characters_written)
    print("Mode:", file_object.mode)
    file_object.close()

    return file_path


def append_file(file_path):
    with open(file_path, "a", encoding="utf-8") as file_object:
        file_object.write("fourth line added with append mode\n")


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file_object:
        print("Full file contents:")
        print(file_object.read())


def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file_object:
        lines = file_object.readlines()

    print("List returned by readlines():")
    print(lines)

    print("Looping through each line:")
    for line in lines:
        print(line.strip())


def show_seek_and_tell():
    file_path = GENERATED_DIR / "myseekfile.txt"

    with open(file_path, "w", encoding="utf-8") as file_object:
        file_object.write("this is for seek test")

    with open(file_path, "r", encoding="utf-8") as file_object:
        print("First read:", file_object.read())
        print("Position after first read:", file_object.tell())

        file_object.seek(0)
        print("Position after seek(0):", file_object.tell())
        print("Second read:", file_object.read())


def main():
    file_path = write_file()
    append_file(file_path)
    print()
    read_file(file_path)
    print()
    read_lines(file_path)
    print()
    show_seek_and_tell()


if __name__ == "__main__":
    main()
