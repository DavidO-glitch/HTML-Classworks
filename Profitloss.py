actual_cost= float(input("Please enter the actual product price: "))
sale_amount= float(input("Please enter the sales amont: "))
if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total profit = ", amount)
else:
    print("No Profit !!")