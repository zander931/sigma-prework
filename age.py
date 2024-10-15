# Age.py compares the number of years between the current date and an inputted date (of birth)
# L3_Challenge_3:_Task_1

from datetime import datetime
# from dateutil.relativedelta import relativedelta


def calculate_age(dob):
    today = datetime.today()
    # Can also use the years attribute from relativedelta imported from the dateutil module:
    # age = relativedelta(today, dob).years
    age = today.year - dob.year - ((today.day, today.month) < (dob.day, dob.month))
    return age


def main():
    dob_input = input("Enter your date of birth (DD-MM-YYYY): ")
    try:
        dob = datetime.strptime(dob_input, "%d-%m-%Y")
        age = calculate_age(dob)
        print(f'You are {age} years old.')
    except ValueError:
        print('Invalid date format. Please use DD-MM-YYYY.')

if __name__ == '__main__':
    main()
