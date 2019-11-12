from faker import Faker
import general
import random
import writer

fake = Faker()
operators = []


def generate_operator():
    import main
    salaries = ["900", "1000", "1200"]
    bday = fake.date_of_birth()
    pesel = general.generate_pesel(bday)
    name = main.divide(fake.name())
    first = name[0]
    surname = name[1]
    salary = random.choice(salaries)
    email = fake.email()
    operator = [pesel, first, surname, salary, email]
    return operator


def new_operators(amount):
    for i in range(amount):
        writer.export_data(generate_operator(), "output/operators.csv")


def import_operator():
    writer.read("output/operators.csv", operators)
    return random.choice(operators)[0]

