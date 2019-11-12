import random
import client
import datetime
import general
import writer
from faker import Faker
import operators

fake = Faker()
the_date = datetime.date(2016, 6, 6)
first = datetime.date(2018, 10, 31)


def generate_call(launch_date):  # This isn't finished, the problem is, that we need to store the date when was call
    satisfaction = random.randint(1, 9)
    response_time = random.randint(3, 120)
    call_date = fake.date_between(start_date=launch_date, end_date="now")
    operator_phone = client.generate_phone('pl')
    call = [satisfaction, response_time, operator_phone, call_date]
    return call


def generate_output():
    deps = []
    writer.read("output/departments.csv", deps)
    pesel = general.generate_pesel(the_date)
    call_id = general.generate_id()
    call = generate_call(the_date)
    writer.export_data([call_id,
                        pesel,
                        deps[random.randint(1, 5)][0],
                        operators.import_operator(),
                        call[0],
                        call[1],
                        call[3]],
                       "output/calls.csv")


