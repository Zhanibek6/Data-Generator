from faker import Faker  # This library is for generating client's information
import random
import writer
import general

fake = Faker()


def generate_client():
    return fake.profile()  #   This generates client's name, surname, mail, address, bday and other stuff that we don't need


def generate_phone():  # Simple phone number generator
    number = ""
    length = 9
    code = "+48"
    for i in range(length):
        number = number + str(random.randint(1, 9))
    return code + number


def generate_output(cli_id):
    person = generate_client()
    pesel = general.generate_pesel(person["birthdate"])
    region = random.choice(["Masovia", "Kuyavia", "Podlasie", "Pemrania", "Pomerelia", "Silesia"])
    person_rows = [cli_id,
                   pesel,
                   person["name"],
                   region,
                   fake.city(),
                   fake.postcode(),
                   fake.street_address(),
                   generate_phone()]
    writer.export_data(person_rows, "output/client.csv")


