import random
import client
import mobile
import datetime
import writer
import call
import internet


def divide(name):
    space = name.find(" ")
    first = name[:space]
    sur = name[space+1:]
    full_name = [first, sur]
    return full_name


def main():
    for i in range(2):
        client.generate_output()
        call.generate_output()
        internet.generate_output()
        mobile.generate_output()
        mobile.client_output()
        internet.client_output()


main()

