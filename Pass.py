for x in range(16):
    if x % 16== 0:
        print("twist")

    elif x % 15 == 0:
        pass

    elif x % 5 == 0:
        print("fizz")

    elif x % 3 == 0:
        print("buzz")

    else:
        print(x)