SECOND_TEMPLATE = "1 second"
SECONDS_TEMPLATE = "{} seconds"
MINUTE_TEMPLATE = "1 minute"
MINUTES_TEMPLATE = "{} minutes"
HOUR_TEMPLATE = "1 hour"
HOURS_TEMPLATE = "{} hours"
DAY_TEMPLATE = "1 day"
DAYS_TEMPLATE = "{} days"
YEAR_TEMPLATE = "1 year"
YEARS_TEMPLATE = "{} years"
COMMA_TEMPLATE = ", "
AND_TEMPLATE = " and "
DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

def format_duration(seconds):
    # your code here
    if seconds == 0:
        return "now"
    years_number = int(seconds / DAYS_IN_YEAR / HOURS_IN_DAY / MINUTES_IN_HOUR / SECONDS_IN_MINUTE)
    years_part = YEAR_TEMPLATE if years_number == 1 else "" if years_number == 0 else YEARS_TEMPLATE.format(years_number)
    days_number = int((seconds - DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE * years_number) / HOURS_IN_DAY / MINUTES_IN_HOUR / SECONDS_IN_MINUTE)
    days_part = DAY_TEMPLATE if days_number == 1 else "" if days_number == 0 else DAYS_TEMPLATE.format(days_number)
    hours_number = int((seconds - DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE * years_number - HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE * days_number) / MINUTES_IN_HOUR / SECONDS_IN_MINUTE)
    hours_part = HOUR_TEMPLATE if hours_number == 1 else "" if hours_number == 0 else HOURS_TEMPLATE.format(hours_number)
    minutes_number = int((seconds - DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE * years_number - HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE * days_number - MINUTES_IN_HOUR * SECONDS_IN_MINUTE * hours_number) / SECONDS_IN_MINUTE)
    minutes_part = MINUTE_TEMPLATE if minutes_number == 1 else "" if minutes_number == 0 else MINUTES_TEMPLATE.format(minutes_number)
    seconds_number = seconds % SECONDS_IN_MINUTE
    seconds_part = SECOND_TEMPLATE if seconds_number == 1 else "" if seconds_number == 0 else SECONDS_TEMPLATE.format(seconds_number)
    if years_number + days_number + hours_number + minutes_number > 0 and seconds_number > 0:
        seconds_part = AND_TEMPLATE + seconds_part
    if years_number + days_number + hours_number > 0 and minutes_number > 0:
        minutes_part = COMMA_TEMPLATE + minutes_part if seconds_number > 0 else AND_TEMPLATE + minutes_part
    if years_number + days_number > 0 and hours_number > 0:
        hours_part = COMMA_TEMPLATE + hours_part if minutes_number + seconds_number > 0 else AND_TEMPLATE + hours_part
    if years_number > 0 and days_number > 0:
        days_part = COMMA_TEMPLATE + days_part if hours_number + minutes_number + seconds_number > 0 else AND_TEMPLATE + days_part
    return years_part + days_part + hours_part + minutes_part + seconds_part
