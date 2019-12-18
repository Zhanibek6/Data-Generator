from faker import Faker
import random
import writer
import datetime
import settings

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
    # price = None
    minute = None
    mb = None
    date = None
    if name == names[0]:
        # price = prices[0]
        minute = minutes[0]
        mb = mbs[0]
        date = launch_date[0]
    elif name == names[1]:
        # price = prices[1]
        minute = minutes[1]
        mb = mbs[1]
        date = launch_date[1]
    elif name == names[2]:
        # price = prices[2]
        minute = minutes[2]
        mb = mbs[2]
        date = launch_date[2]

    return [name, date, minute, mb]


first = datetime.date(2018, 10, 31)


def generate_output(mobile_id):
    plan = generate_plan()
    # expiration_date = fake.date_between(start_date=plan[1], end_date='now')
    launch_date = random.randint(365, 720)
    expiration_date = random.randint(launch_date, 1400)
    writer.export_data([mobile_id+14, plan[0], expiration_date, launch_date], settings.location+"mobile_plans.csv")


t_one = datetime.date(2018, 1, 1)

'''
def client_output():
    plan = generate_plan()
    numeric_id = general.generate_id()
    mb_id = general.generate_id()
    # pesel = general.generate_pesel(fake.date_of_birth())
    contract = fake.date_between(start_date=plan[1], end_date=t_one)
    permanence = fake.date_between(start_date=contract, end_date=t_one)
    client_mobile = [numeric_id, mb_id, contract, permanence, plan[2], plan[3]]
    writer.export_data(client_mobile, "output/client_mobile.csv")
'''


def having_mp():
    old_chance = random.randint(1, 100)
    if old_chance < 20:
        client = writer.get_row("output/T0-T1/having_mp.csv",
                                random.randint(1, writer.count_row("output/T0-T1/having_mp.csv"))-1)
        cli_id = client[2]
        phone = client[0]
    else:
        client = writer.get_row(settings.location+"client.csv",
                                random.randint(1, writer.count_row(settings.location+"client.csv")-1))
        cli_id = client[0]
        phone = client[7]
    mb_plan = writer.get_row(settings.location + "mobile_plans.csv",
                             random.randint(1, writer.count_row(settings.location + "mobile_plans.csv")-1))
    mb_id = mb_plan[0]
    contract = random.randint(365, 720)
    mp = [phone,
          mb_id,
          cli_id,  # The id itself
          contract,  # The date
          random.randint(contract, 1400),
          random.choice([200, 250, 350, 400]),  # Price
          random.choice([" ", 500, 400, 600, 700, 800]),  # Minutes
          random.choice([" ", 100, 200, 300, 400, 500])  # Internet
          ]
    writer.export_data(mp, settings.location+"having_mp.csv")


for i in range(1000):
    having_mp()
