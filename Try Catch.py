try:
    num1, num2 = eval(input("Enter two numbers, seperated by a coma : "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Coma is  missinG. Enter numbers seperated by coma like this 1,2")

except:
    print("Wrong Input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")