import datetime, random, calendar
from datetime import date

def date_information():
    current_year = date.today().year
    random_year = random.randint(current_year - 10, current_year - 1)
    random_month = random.randint(1, 12)

    # Get the maximum number of days for the selected month
    max_days = calendar.monthrange(random_year, random_month)[1]

    # Generate a random day within the valid range for the selected month
    random_day = random.randint(1, max_days)
    return date(random_year, random_month, random_day)