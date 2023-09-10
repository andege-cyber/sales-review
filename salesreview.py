products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#calculate the total price average for all products
total = sum(prices)    #total price
print("Total = ", total)
print()
average = sum(prices)/len(prices)   #average price
print("Average =", round(average, 2)) #rounded off average to 2 decimal places
print()

#calculate the average daily revenue generated from the products
daily_revenue= [prices[r]/last_week[r] for r in range(len(prices))]
rounded_off = [round(t) for t in daily_revenue]   #rounds of values of daily-revenue to a whole number
print("Average daily revenue= ", rounded_off)
print()

#create a new price list that reduces the old prices by $ 5
for p in range(len(prices)):
    prices[p] -= 5

print("New price list=", prices)
print()

#calculate the total revenue generated from the products
newtotal= sum(prices)
print("New total =", newtotal)
print()

#based on the new prices, which products are less than $ 30 
price_dict={"Sankofa Foods":25,
           "Jamestown Coffee":20,
           "Bioko Chocolate":35,
           "Blue Skies Ice Cream":15,
           "Fair Afric Chocolate":15,
           "Kawa Moka Coffee":30,
           "Aphro Spirit":40,
           "Mensado Bissap":45,
           "Voltic":30
           }
#print(price_dict)
for key, value in price_dict.items():
    if value < 30:
     print(key)