import random
import client
import datetime
import general
import writer
from faker import Faker

fake = Faker()
the_date = datetime.date(2016, 6, 6)


def generate_call(launch_date):  # This isn't finished, the problem is, that we need to store the date when was call
    satisfaction = random.randint(1, 9)
    response_time = random.randint(3, 120)
    call_date = fake.date_between(start_date=launch_date, end_date="now")
    operator_phone = client.generate_phone('pl')
    call = [satisfaction, response_time, operator_phone, call_date]
    return call


def generate_output():
    pesel = general.generate_pesel("2010, 1, 1")
    call_id = general.generate_id()
    call = generate_call(the_date)
    writer.export_data([call_id,
                        pesel,
                        "Here should be department id",
                        call[0],
                        call[1],
                        call[2],
                        call[3]], "calls.csv")


