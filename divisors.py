user_int = int(input('enter a num: '))
results = []


def divisor(i):
    for n in range(1, (i + 1)):
        if i % n == 0:
            results.append(n)


divisor(user_int)
print(results)
