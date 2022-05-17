#Milestone assignment: calculating the price of a meal
meal_kids = float(input("What is the price of a child's meal?"))
meal_adults = float(input("What is the price of an adult's meal?"))
number_children= int(input ("How many children are there?"))
number_adults = int(input ("How many adults are there?"))
tax= float(input("What is the sales tax rate?"))

total_cost = (meal_kids * number_children) + (meal_adults * number_adults)
print("Subtotal:$  " + str(total_cost))

sales_tax= (total_cost * 6) / 100 
print("Sales Tax:$ " + str(sales_tax))

total_price= (total_cost)+ (sales_tax)
print("Total:$ " + str(total_price))

payment_amount =  float(input("What is the payment amount?"))
change = str(payment_amount - total_price)
print("Change:$" + str(change))
print ('✓✓')



