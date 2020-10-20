import random

list = []


def create_random_list():
    """ Create a random list of 99 integers between 1 and 99. """

    for i in range(0, 99):
        n = random.randint(1, 100)
        list.append(n)

    print(list)


def list_parse(given_list):
    """ Parse the rasndom list and return int's less than user inputted number. """

    less_than_list = []
    user_input = int(input('Less that how many?? '))

    for n in given_list:
        if n < user_input:
            less_than_list.append(n)

    print(less_than_list)


create_random_list()
list_parse(list)
