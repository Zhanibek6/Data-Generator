import random
import string
import writer
import general
import mobile
import datetime
from faker import Faker
#   An alphanumeric code generator
fake = Faker()


def generate_departments():
    names = ["Sales", "Maintenance", "Support", "Anti-Cancellation"]
    name = random.choice(names)

    return [name]
    
deps = generate_departments()


def generate_output():
    numeric_id = general.generate_id()
    departments = [numeric_id, name]
    writer.export_data(departments, "output/departments.csv")
