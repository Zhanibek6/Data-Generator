import random
import datetime
import writer
from faker import Faker
import settings

fake = Faker()
the_date = datetime.date(2018, 1, 1)
first = datetime.date(2018, 10, 31)


def generate_call():  # This isn't finished, the problem is, that we need to store the date when was call
    satisfaction = random.randint(1, 9)
    response_time = random.choice(["SHORT", "ACCEPTABLE", "EXCESSIVE"])
    # call_date = fake.date_between(start_date=launch_date, end_date="now")
    # operator_phone = client.generate_phone()
    call = [satisfaction, response_time]
    return call


def generate_output(call_id):
    call = generate_call()
    writer.export_data([call_id+settings.additional_id_calls,
                        call[0],
                        call[1]],
                       settings.location+"/calls.csv")

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
        departments = ["DEPT_SALES", "DEPT_MAIN", "DEPT_SUPPORT", "DEPT_CANCEL"]
        if settings.location == "output/T1-T2/":
            departments.append("DEPT_UPDATE")
            departments.append("DEPT_UPGRADE")
        dept_id = random.choice(departments) # "DEPT_UPGRADE"])
        client_id = writer.get_row(settings.location+"/client.csv",
                                   random.randint(1, writer.count_row(settings.location+"/client.csv")-1))[0]
        tele_id = writer.get_row(settings.location+"/operators.csv",
                                 random.randint(1, writer.count_row(settings.location+"/operators.csv")-1))
        call = writer.get_row(settings.location+"/calls.csv",
                              random.randint(1, writer.count_row(settings.location+"/calls.csv")-1))
        date = random.randint(1, settings.days_count)
        satisfaction = call[1]
        response = call[2]
        if response == "SHORT":
            response = random.randint(0, 3)
        elif response == "ACCEPTABLE":
            response = random.randint(3, 6)
        else:
            response = random.randint(6, 10)
        salary = tele_id[3]
        call = [some_id+settings.additional_id_calls,
                client_id,
                dept_id,
                tele_id[0],
                salary,
                date,
                satisfaction,
                response]
        writer.export_data(call, settings.location+"/answer.csv")


#
for i in range(4001):
    answer_call(i)


