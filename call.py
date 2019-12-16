import random
import client
import datetime
import general
import writer
from faker import Faker

fake = Faker()
the_date = datetime.date(2016, 6, 6)
first = datetime.date(2018, 10, 31)


def generate_call(launch_date):  # This isn't finished, the problem is, that we need to store the date when was call
    satisfaction = random.randint(1, 9)
    response_time = random.choice(["SHORT", "ACCEPTABLE", "EXCESSIVE"])
    # call_date = fake.date_between(start_date=launch_date, end_date="now")
    # operator_phone = client.generate_phone()
    call = [satisfaction, response_time]
    return call


def generate_output(call_id):
    call = generate_call(the_date)
    writer.export_data([call_id,
                        call[0],
                        call[1]],
                       "output/calls.csv")

'''
def answer_call():
    dept_id = random.choice(["DEPT_SALES", "DEPT_MAIN", "DEPT_SUPPORT", "DEPT_CANCEL", "DEPT_UPGRADE"])
    call = generate_call(the_date)
    client_id = general.generate_id()
    call_id = general.generate_id()
    tele_id = general.generate_id()
    satisfaction = call[0]
    response = call[1]
    salary = random.choice(["900", "1000", "1200"])
    call = [call_id, client_id, dept_id, tele_id, salary, satisfaction, response]
    writer.export_data(call, "output/fact1.csv")
'''


def answer_call(some_id):
    if some_id != 0:
        dept_id = random.choice(["DEPT_SALES", "DEPT_MAIN", "DEPT_SUPPORT", "DEPT_CANCEL", "DEPT_UPGRADE"])
        client_id = random.randint(0, 1400)
        tele_id = random.randint(0, 1400)
        call = writer.get_row("output/calls.csv", client_id)
        date = client_id
        satisfaction = call[1]
        response = call[2]
        salary = writer.get_row("output/operators.csv", random.randint(1, 100))[3]
        call = [some_id, client_id, dept_id, tele_id, salary, date, satisfaction, response]
        writer.export_data(call, "output/answer.csv")
