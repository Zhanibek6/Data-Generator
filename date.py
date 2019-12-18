import random
from faker import Faker
import calendar
import writer
import settings

fake = Faker()

'''
def generate_date(date_id):
    starting_date = fake.date_between(start_date="2016.01.01", end_date="")
    year = random.choice([2016, 2017, 2018])
    month = fake.month()
    fake_date = str(year) + "," + month + "," + str(date_id+1)
    date = [date_id,
            random.randint(1, 4),
            year,
            calendar.month_name[int(month)],
            fake_date]
    writer.export_data(date, "output/date.csv")
'''


def generate_date():
    '''
    months = {v: k for k, v in enumerate(calendar.month_abbr)}
    if settings.location == "output/T1-T2/":
        previous = writer.get_row("output/T0-T1/date.csv", writer.count_row("output/T0-T1/date.csv")-1)
        additional_id = previous[0]
        quarter = previous[1]
        start_year = previous[2]
        start_month = months[previous[3][:3]]
        start_day = previous[4]
    else:
    '''
    start_year = settings.starting_year
    start_month = 3
    start_day = 17
    quarter = 1
    additional_id = 720
    for i in range(settings.days_count):
        if start_month == 2:
            days = 28
        elif (start_month % 2) == 0:
            days = 30
        else:
            days = 31
        if start_day >= days:
            start_day = 1
            start_month = start_month + 1
        if start_month > 3:
            quarter = 2
        if start_month > 6:
            quarter = 3
        if start_month > 9:
            quarter = 4
        if start_month >= 12:
            start_month = 1
            start_year = start_year + 1
            quarter = 1
        date = str(start_year) + "-" + str(start_month) + "-" + str(start_day)
        start_day = start_day + 1
        writer.export_data([i+additional_id,
                            quarter,
                            start_year,
                            calendar.month_name[start_month],
                            date],
                           settings.location+"/date.csv")


generate_date()