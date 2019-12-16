import client
import mobile
import call
import internet
import date


def divide(name):
    space = name.find(" ")
    first = name[:space]
    sur = name[space+1:]
    full_name = [first, sur]
    return full_name


def main(i):
    client.generate_output(i)
    call.generate_output(i)
    date.generate_date(i)
    internet.generate_output(i)
    internet.client_output()
    mobile.generate_output(i)
    mobile.client_output()

'''
for i in range(2000):
    main(i)
'''

for i in range(2000):
    mobile.having_mp()
    internet.having_ip()
    call.answer_call(i)
