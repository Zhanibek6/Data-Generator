import random
import string
import writer
import general
import mobile
import datetime
from faker import Faker
#   An alphanumeric code generator


'''
Here we have info about three plans, with their names, prices, minutes, etc...
'''

fake = Faker()
first = datetime.date(2018, 12, 31)


def generate_internet_plan():
    names = ["200Mb", "500Mb", "1000Mb"]
    # we can use other representative names for them...
    prices = [90, 150, 300]  # PLN
    minutes = [200, 400, -1]  # -1 means unlimited
    bandwidth = [200, 500, 1000]  # in Mb/s
    launch_date = [datetime.date(2016, 6, 6), datetime.date(2017, 7, 7), datetime.date(2018, 8, 8)]
    expiration_date = [datetime.date(2018, 6, 6), datetime.date(2018, 7, 7), datetime.date(2018, 8, 8)]
    name = random.choice(names)
    price = None
    expiration = None
    mb = None
    date = None
    if name == names[0]:
        price = prices[0]
        expiration = expiration_date[0]
        mb = bandwidth[0]
        date = launch_date[0]
    elif name == names[1]:
        price = prices[1]
        expiration = expiration_date[0]
        mb = bandwidth[1]
        date = launch_date[1]
    elif name == names[2]:
        price = prices[2]
        expiration = expiration_date[0]
        mb = bandwidth[2]
        date = launch_date[2]

    return [name, mb, expiration, date]


def generate_output(i_id):
    plan = generate_internet_plan()
    contract_date = fake.date_between(start_date=plan[3], end_date='now')
    # expiration_date = mobile.fake.date_between(start_date=contract_date, end_date='now')
    expiration_date = random.randint(0, 10)
    internet_plan = [i_id, plan[0], plan[1], expiration_date, random.randint(0, 10)]
    writer.export_data(internet_plan, "output/internet_plans.csv")


def client_output():
    plan = generate_internet_plan()
    numeric_id = general.generate_id()
    i_id = general.generate_id()
    pesel = general.generate_pesel(fake.date_of_birth())
    contract = fake.date_between(start_date=plan[3], end_date='now')
    permanence = fake.date_between(start_date=contract, end_date='now')
    expiration = fake.date_between(start_date=permanence, end_date='now')
    client_mobile = [numeric_id, i_id, contract, permanence, expiration, plan[2], plan[4]]
    writer.export_data(client_mobile, "output/client_int.csv")


for i in range(10):
    generate_output(i)