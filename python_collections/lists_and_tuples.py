# Lists and Tuples

# Making a list in Python

shopping_list = ["eggs", "bacon", "bananas", "bread", "haggis"]

print(type(shopping_list))
print(shopping_list)

# Accessing certain parts of the list

print(shopping_list[0])
print(shopping_list[4])
print(shopping_list[-1])

# Change a specific element of the list

shopping_list[4] = "orange juice"
print(shopping_list)

# List methods

shopping_list.append("butter")
print(shopping_list)

shopping_list.remove("butter")
print(shopping_list)

shopping_list.pop() # removes the final item from the list
print(shopping_list)

shopping_list.pop()
print(shopping_list)

shopping_list.pop(1)
print(shopping_list)

x = shopping_list.pop(0)
print(x)

# Mixed data type list

mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)

# List slicing

print(mixture[1:3])
print(mixture[::2]) # every second step
print(mixture[::3]) # every third step

# Tuples are immutable so they cannot be changed

essentials = ("bread", "eggs", "milk")
print(type(essentials))
print(essentials)
print(essentials.count("bread"))