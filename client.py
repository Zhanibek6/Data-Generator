from faker import Faker  # This library is for generating client's information
import random
import writer
import general

fake = Faker()


def generate_client():
    return fake.profile()  #  This generates client's name, surname, mail, address, bday and other stuff that we don't need


def generate_phone(country):  # Simple phone number generator
    code = None
    number = ""
    length = 9
    if country == "us":
        code = "+1"
        length = "10"
    elif country == "ru":
        code = "+7 7"
    elif country == "pl":
        code = "+48"
    for i in range(length):
        number = number + str(random.randint(1, 9))
    return code + number


def generate_output():
    import main
    person = generate_client()
    pesel = general.generate_pesel(person["birthdate"])
    person_rows = [pesel,
                   main.divide(person["name"])[0],
                   main.divide(person["name"])[1],
                   person["mail"],
                   person["residence"].replace("\n", " "),
                   generate_phone("pl")]
    writer.export_data(person_rows, "output/client.csv")

