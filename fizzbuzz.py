def fizzle(y):
    for a in range(1, (y + 1)):
        if a % 3 == 0 and a % 5 == 0:
            print("FIZZBUZZ")
        elif a % 3 == 0:
            print("FIZZ")
        elif a % 5 == 0:
            print("BUZZ")
        else:
            print(a)


y = int(input('how many fizzbuzzes? '))

fizzle(y)
