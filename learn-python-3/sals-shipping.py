# input weight and the terminal will display the cost of using Sal's Shippers

"""
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

"""



weight = 4.8

# ground shipping
if weight <= 2:
  price_per_pound = 1.50
elif weight <=6:
  price_per_pound = 3.00
elif weight <= 10:
  price_per_pound = 4.00
elif weight > 10:
  price_per_pound = 4.75
else:
  print('please write a valid number for weight')

flat_charge = 20
ground_shipping_cost = weight * price_per_pound + flat_charge

print(f'Cost of ground shipping: ${ground_shipping_cost}')

# ground shipping premium
ground_shipping_premium_cost = 125

print(f'Cost of ground shipping premium: ${ground_shipping_premium_cost}')

# drone shipping
if weight <= 2:
  price_per_pound = 4.50
elif weight <=6:
  price_per_pound = 9
elif weight <= 10:
  price_per_pound = 12
elif weight > 10:
  price_per_pound = 14.25
else:
  print('please write a valid number for weight')

drone_shipping_cost = weight * price_per_pound

print(f'Cost of drone shipping: ${drone_shipping_cost}')


# cheapest method

