import client
import mobile
import call
import internet
import settings


def divide(name):
    space = name.find(" ")
    first = name[:space]
    sur = name[space+1:]
    full_name = [first, sur]
    return full_name


def main(i):
    client.generate_output(i)
    call.generate_output(i)


for i in range(settings.amount_call_client):
    main(i)

for i in range(settings.amount_of_plans):
    internet.generate_output(i)
    mobile.generate_output(i)

for i in range(settings.amount_having_ip_mp):
    mobile.having_mp()
    internet.having_ip()
    call.answer_call(i)
