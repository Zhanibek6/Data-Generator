from faker import Faker
import general
import random
import writer

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
    operator = [i+250, pesel, fake.name(), salary, valid]
    return operator


def new_operators(amount):
    for i in range(amount):
        writer.export_data(generate_operator(i), "output/T1-T2/operators.csv")


def import_operator():
    writer.read("output/operators.csv", operators)
    return random.choice(operators)[0]


new_operators(150)
