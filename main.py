import random
import client
import mobile
import datetime
import writer
import call
import internet
import departments


def divide(name):
    space = name.find(" ")
    first = name[:space]
    sur = name[space+1:]
    full_name = [first, sur]
    return full_name


def main():
    client.generate_output()
    call.generate_output()
    internet.generate_output()
    internet.client_output()
    mobile.generate_output()
    mobile.client_output()


main()
