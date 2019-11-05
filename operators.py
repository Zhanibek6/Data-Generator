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


'''
writer.export_data("12314153324234", "operators.csv")
for i in range(30):
    writer.export_data(general.generate_pesel(fake.date_of_birth()), "operators.csv")
'''