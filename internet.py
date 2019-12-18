import random
import string
import writer
import general
import mobile
import datetime
from faker import Faker
import settings


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
    bandwidth = ["low", "medium", "high"]  # in Mb/s
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
    # contract_date = fake.date_between(start_date=plan[3], end_date='now')
    contract_date = random.randint(365, 720)
    expiration_date = random.randint(contract_date, 1400)
    # expiration_date = mobile.fake.date_between(start_date=contract_date, end_date='now')
    internet_plan = [i_id+14, plan[0], plan[1], expiration_date, contract_date]
    writer.export_data(internet_plan, settings.location+"internet_plans.csv")


t_one = datetime.date(2018, 1, 1)

'''
def client_output():
    plan = generate_internet_plan()
    numeric_id = general.generate_id()
    i_id = general.generate_id()
    pesel = general.generate_pesel(fake.date_of_birth())
    contract = fake.date_between(start_date=plan[3], end_date=t_one)
    permanence = fake.date_between(start_date=contract, end_date=t_one)
    expiration = fake.date_between(start_date=permanence, end_date=t_one)
    client_mobile = [numeric_id, i_id, contract, permanence, expiration, plan[2], plan[3]]
    writer.export_data(client_mobile, "output/client_int.csv")
'''


def having_ip():
    old_chance = random.randint(1, 100)
    if old_chance < 30:
        client = writer.get_row("output/T0-T1/having_ip.csv",
                                random.randint(1, writer.count_row("output/T0-T1/having_ip.csv") - 1))
        phone = client[0]
        cli_id = client[1]
    else:
        client = writer.get_row(settings.location + "client.csv",
                                random.randint(1, writer.count_row(settings.location + "client.csv") - 1))
        phone = client[7]
        cli_id = client[0]
    ip_plan = writer.get_row(settings.location + "internet_plans.csv",
                             random.randint(1, writer.count_row(settings.location + "internet_plans.csv") - 1))
    i_id = ip_plan[0]
    contract = random.randint(365, 720)
    ip = [phone,
          cli_id,  # The id itself
          i_id,
          contract,  # The date
          random.randint(contract, 1400),  # Permanence
          random.choice([100, 150, 200, 250, 300, 350, 400]),  # Price
          random.choice([" ", 300, 400, 500]),  # Minutes
          ]
    writer.export_data(ip, settings.location+"having_ip.csv")


for i in range(1000):
    having_ip()
'''
for i in range(5):
    generate_output(i)
'''
