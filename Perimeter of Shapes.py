def perimeter_Square(number):
    return number * 4

def perimeter_rctangle(number1, number2):
    return 2* (number1 + number2)

def perimeter_trinagle(side1, side2, side3):
    return side1 + side2 + side3

def perimeter_parallelogram(base, height):
    return 2 * (base + height)

print(perimeter_Square(7))

print(perimeter_trinagle(3,5,7))

print(perimeter_parallelogram(2,4))


print(perimeter_rctangle(6,4))  
