from datetime import datetime, timedelta
from random import randint
import re

######################################################################
# 1 task
# Returns : number of days between the 'date' and today
#           if there are errors in the input data - None
# date : a string representing a date in the format 'YYYY-MM-DD'
def get_days_from_today(date: str) -> int:

    try:
        date_input = datetime.strptime(date, '%Y-%m-%d')
    except:
        print("Format should be: 'YYYY-MM-DD'")
        return None

    return datetime.today().date().toordinal() - date_input.toordinal()

######################################################################
# 2 task
# Returns : set of random numbers within given parameters, and all numbers in the set must be unique
#           if there are errors in the input data - None
# min : the minimum possible number in the set (at least 1)
# max : the maximum possible number in the set (no more than 1000)
# quantity : number of numbers to choose (value between min and max)
def get_numbers_ticket(min: int, max: int, quantity: int):

    if ((max - quantity) < min) or (min < 1) or (max > 1000) or (quantity <= 0):
        print("min should be: at least 1")
        print("max should be: no more than 1000")
        print("quantity should be: more than 0")
        print("(max - quantity) should be: >= min")
        return None

    set_numbers = set()
    while len(set_numbers) < quantity:
        set_numbers.add(randint(min, max))

    list_numbers = list(set_numbers)
    list_numbers.sort()

    return list_numbers

######################################################################
# 3 task
# Returns : normalized phone number as a string
# phone_number : string with a phone number in various formats
def normalize_phone(phone_number: str) -> str:

    re.sub('\D', '', 'aas30dsa20')
    normalized_phone_number = re.sub('\D', '', phone_number)

    if len(normalized_phone_number) == 10:
        normalized_phone_number = '+38' + normalized_phone_number
    elif len(normalized_phone_number) == 12:
        normalized_phone_number = '+' + normalized_phone_number
    return normalized_phone_number

######################################################################
# 4 task
# Returns : collected data as a list of dictionaries with usernames and greeting dates
# users : list of dictionaries, where each dictionary contains:
#       - name (user name)
#       - birthday (date of birth in the string format 'yyyy.mm.dd').
def get_upcoming_birthdays(users):

    today = datetime.today().date()
    first_day = today + timedelta(days = 1)
    last_day  = today + timedelta(days = 7)
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime(year = first_day.year, month = birthday.month, day = birthday.day).date()

        if birthday_this_year < first_day:
            birthday_this_year = datetime(year = last_day.year, month = birthday.month, day = birthday.day).date()

        birthday_weekday = birthday_this_year.weekday()

        if (birthday_weekday == 5) or (birthday_weekday == 6):
            birthday_this_year = birthday_this_year + timedelta(days = (7 - birthday_weekday))

        if first_day <= birthday_this_year <= last_day:
            upcoming_birthdays.append({'name': user['name'], 'congratulation_date': birthday_this_year.strftime("%Y.%m.%d")})

    return upcoming_birthdays

######################################################################
def main():

    # 1 task
    num_days = get_days_from_today("2022-02-24")
    if not(num_days is None):
        print(num_days)

    # 2 task
    lottery_numbers = get_numbers_ticket(1, 36, 5)
    if not(lottery_numbers is None):
        print("Lottery numbers: ", lottery_numbers)

    # 3 task
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    normalized_phone_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Normalized phone numbers for SMS sending: ", normalized_phone_numbers)

    # 4 task
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"}
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("This week's list of greetings:", upcoming_birthdays)

if __name__ == "__main__":
    main()
