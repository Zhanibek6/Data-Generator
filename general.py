import random
import string
from faker import Faker

fake = Faker()


def generate_id():
    key_id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    return key_id


def generate_pesel(bday):
    number = ""
    year = fake.year()
    year_str = str(year)[:-2]
    month = fake.month()
    day = str(random.randint(1, 31))
    number.join(year_str + month + day)
    for i in range(11):
        number = number + str(random.randint(1, 9))
    return number
