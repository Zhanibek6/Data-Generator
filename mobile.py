from faker import Faker
import random
import string
import writer
import general
import datetime
#   An alphanumeric code generator


'''
Here we have info about three plans, with their names, prices, minutes, etc...
'''
fake = Faker()


def generate_plan():
    names = ["Essential", "Magneta", "Magneta Plus"]
    prices = [30, 50, 60]  # PLN
    minutes = [100, 120, -1]  # -1 means unlimited
    mbs = [15, 20, 25]  # in Gb
    launch_date = [datetime.date(2016, 6, 6), datetime.date(2017, 7, 7), datetime.date(2018, 8, 8)]
    # TO-DO we need to add launched date just like the prices, minutes, etc...
    name = random.choice(names)
    price = None
    minute = None
    mb = None
    date = None
    if name == names[0]:
        price = prices[0]
        minute = minutes[0]
        mb = mbs[0]
        date = launch_date[0]
    elif name == names[1]:
        price = prices[1]
        minute = minutes[1]
        mb = mbs[1]
        date = launch_date[1]
    elif name == names[2]:
        price = prices[2]
        minute = minutes[2]
        mb = mbs[2]
        date = launch_date[2]

    return [name, price, minute, mb, date]


def generate_output():
    numeric_id = general.generate_id()
    plan = generate_plan()
    expiration_date = fake.date_between(start_date=plan[4], end_date='now')
    writer.export_data([numeric_id, plan[0], plan[1], plan[2], expiration_date, plan[3]], "output/mobile_plans.csv")
