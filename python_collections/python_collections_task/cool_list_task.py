# 1. Cool List Task

euromillions_spending_spree = ["house", "holiday", "expensive whisky", "Mediterranean villa", "PS VR2", "4K UHD TV"]

# First, print the list and check its type
print(type(euromillions_spending_spree))
print(euromillions_spending_spree)

# Print the list's first element
print(euromillions_spending_spree[0])

# Print the list's second element
print(euromillions_spending_spree[1])

# Print the list's last element using negative indexing
print(euromillions_spending_spree[-1])

# Replace the first item in the list
euromillions_spending_spree[0] = "car"

# Replace another item in the list and print the list
euromillions_spending_spree[2] = "vans shoes"
print(euromillions_spending_spree)

# Add a new item to the list, print the list
euromillions_spending_spree.append("WWFC shirt")
print(euromillions_spending_spree)

# Remove an item from the list, print the list
euromillions_spending_spree.remove("PS VR2")
print(euromillions_spending_spree)

# Remove the last item from the list without specifying what it is
euromillions_spending_spree.pop()
