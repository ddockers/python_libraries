# 2. Waiter Helper task

"""
User stories:

As a user, I want to be able to see the menu in a formatted way so that I can order my meal.
As a user, I want to be able to order three separate times and have my responses added to a list so they are not forgotten.
As a user, I want to have my order read back to me in a formatted way so I know what I ordered.
"""

starters = ["Vegetable Pakoras", "Chicken Pakoras", "Chicken Wings", "Paneer Salad"]
mains = ["Chicken Bhuna", "Beef Madras", "Beef Jalfrezi", "Vegetable Korma", "Vegetable Biriyani"]
desserts = ["Mango Sorbet", "Chocolate Ice Cream", "Mixed Fruit Salad", "Chocolate Fudge Cake"]

print(starters)
print(mains)
print(desserts)

# First order
print(starters[0])
print(mains[2])
print(desserts[1])

# Second order
print(starters[3])
print(mains[4])
print(desserts[0])

# Third order
print(starters[2])
print(mains[0])
print(desserts[3])

order_1 = [starters[0] + mains[2] + desserts[1]]
print(order_1)

order_2 = [starters[3] + mains[4] + desserts[0]]
print(order_2)

order_3 = [starters[2] + mains[0] + desserts[3]]
print(order_3)

# Make it so that the user can input their order