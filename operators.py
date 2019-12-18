from faker import Faker
import general
import random
import writer
import settings

fake = Faker()
operators = []


def generate_operator(i):
    # import main
    bday = fake.date_of_birth()
    pesel = general.generate_pesel(bday)
    # name = main.divide(fake.name())
    # first = main.divide(name[0])
    # surname = main.divide(name[1])
    salary = random.choice(["900", "1000", "1200"])
    # email = fake.email()
    valid = random.choice([0, 1])
    operator = [i, pesel, fake.name(), salary, valid]
    return operator


def new_operators(amount):
    for i in range(amount):
        writer.export_data(generate_operator(i), settings.location+"/operators.csv")


def import_operator():
    writer.read(settings.location+"/operators.csv")
    return random.choice(operators)[0]


new_operators(150)
