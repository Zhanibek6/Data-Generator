import client
import mobile
import call
import internet


def divide(name):
    space = name.find(" ")
    first = name[:space]
    sur = name[space+1:]
    full_name = [first, sur]
    return full_name


def main(i):
    client.generate_output(i)
    call.generate_output(i)
    internet.generate_output(i)
    internet.client_output()
    mobile.generate_output(i)
    mobile.client_output()


for i in range(100):
    main(i)
