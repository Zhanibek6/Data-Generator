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


def generate_departments():
    names = ["Sales", "Maintenance", "Support", "Anti-Cancellation"]
    # we can use other representative names for them...
    name = random.choice(names)

    return [name]


deps = generate_departments()


def generate_output():
    numeric_id = general.generate_id()
    departments = [numeric_id, name]
    writer.export_data(departments, "output/departments.csv")
