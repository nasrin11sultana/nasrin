def convert_days(days):
    years = days // 365
    days_remaining = days % 365
    months = days_remaining // 30
    weeks = (days_remaining % 30) // 7
    days_left = (days_remaining % 30) % 7
    return years, months, weeks, days_left

days = int(input("Enter number of days: "))
years, months, weeks, days_left = convert_days(days)
print(f"Years: {years}, Months: {months}, Weeks: {weeks}, Days: {days_left}")
