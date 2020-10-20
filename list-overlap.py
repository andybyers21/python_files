import random


def create_random_list(list):
    """ Create a random list of up to 20 integers between 1 and 20. """

    for i in range(0, random.randint(1, 20)):
        n = random.randint(1, 21)
        list.append(n)

    return list


a = []
b = []

create_random_list(a)
create_random_list(b)

print(f"list a: {a}")
print(f"list b: {b}")

results = []

for n in a:
    if n in b:
        results.append(n)

results = list(dict.fromkeys(results))

print(f"results: {results}")
