#

#== Same                       print(name == "All is Fair and Just")
#!= Different                  print(name != "All is Fair and Just")
#> Greater than                print(name > "All is Fair and Just")
#< Less than                   print(name < "All is Fair and Just")
#>= Greater than or equal to   print(name >= "All is Fair and Just")
#<= Less than or equal to      print(name <= "All is Fair and Just")
#>= Greater than or equal to   print(name >= "All is Fair and Just")

#Practical Assesment 
                                                                             
# 5 Student/Person Information meaning date of birth, name, age,
# Input for a Date 
# Output all 5 Student/Person Information and age on the imputed date 
# *Displays any current birthdays 

import datetime

People = [
    {"name": "John", "Birthday": "02/08/2002"},
    {"name": "Walter",  "Birthday": "28/06/2005"},
    {"name": "Tom", "Birthday": "15/01/2007"},  
    {"name": "Jerry", "Birthday": "22/05/2000"},
    {"name": "Alice", "Birthday": "10/12/1990"}
]

Date = input("Enter the date (DD/MM/YYYY): ")


Date = datetime.datetime.strptime(Date, "%d/%m/%Y")

print("\nPeople Information:")
print("-" * 50)

birthdays_today = []

for person in People:
    name = person["name"]
    birthday = datetime.datetime.strptime(person["Birthday"], "%d/%m/%Y")

    age = Date.year - birthday.year

    if (Date.month, Date.day) < (birthday.month, birthday.day):
        age -= 1
    print(f"Name: {name}, Birthday: {person['Birthday']}, Age: {age}")

    
    if Date.month == birthday.month and Date.day == birthday.day:
        birthdays_today.append(name)

print("-" * 50)

if birthdays_today:
    print(f"Birthday is  today: {', '.join(birthdays_today)}")