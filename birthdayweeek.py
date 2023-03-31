
import datetime
import calendar

now = datetime.datetime.now()
current_year = now.year

def get_birthdays(cyear,byear,month,day):

    try:
        weekday_index = calendar.weekday(cyear,month,day)
    except:
        print("\nERROR:")
        print("Please enter DAY correctly\n")
        day, month, year = birthdayinput()

    dayname = calendar.day_name[weekday_index]
    age = cyear - byear
    return age, dayname

print(""""
Enter your birthday
Example: 23/09/2020
""""")

def birthdayinput():

    birthday = input("Your birthday: ")

    try:
        day, month, year = birthday.split("/")

    except:
        print("\nERROR:")
        print("The correct format of entering date of birth is-dd/mm/yyyy\n")
        day, month, year = birthdayinput()

    try:
        day = int(day)
        month = int(month)
        year = int(year)

    except ValueError:
        print("\nERROR:")
        print("Please enter DIGITS.\n")
        day, month, year = birthdayinput()

    if month > 12:
        print("\nERROR:")
        print("Please enter correct birth MONTH\n")
        day, month, year = birthdayinput()

    if year >= current_year:
        print("\nERROR:")
        print("Please enter correct birth YEAR\n")
        day, month, year = birthdayinput()

    return calculatebirthday(day, month, year)

def calculatebirthday(day, month, year):

    global current_year
    print(f"\n{39*'_'}")

    while (current_year - year) >= 0:

        age, dayname = get_birthdays(current_year, year, month, day)

        print(f"Year: {current_year} | Age: {age} | Day - {dayname}")
        current_year -= 1

    print(f"{39*'_'}")
    return age, dayname

try:
    day, month, year = birthdayinput()
except:
    pass

