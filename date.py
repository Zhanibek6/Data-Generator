import random
from faker import Faker
import calendar
import writer


fake = Faker()


def generate_date(date_id):
    year = random.choice([2016, 2017, 2018])
    month = fake.month()
    fake_date = str(year) + "," + month + "," + str(random.randint(1, 31))
    date = [date_id,
            random.randint(1, 4),
            year,
            calendar.month_name[int(month)],
            fake_date]
    writer.export_data(date, "output/date.csv")


