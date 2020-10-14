def fizz(x, y):
    for a in range(x, y):
        if a % 3 == 0 and a % 5 == 0:
            print("FIZZBUZZ")
        elif a % 3 == 0:
            print("FIZZ")
        elif a % 5 == 0:
            print("BUZZ")
        else:
            print(a)


fizz(1, 50)
