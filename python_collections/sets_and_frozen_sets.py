# Sets and Frozen Sets

# {} - List but unordered

car_parts = {"wheels", "windows", "exhaust", "steering wheel"}
print(car_parts) # each time this runs the order is different

# add to a set

car_parts.add("doors")
print(car_parts)

# remove from a set

car_parts.remove("doors")
print(car_parts)

# frozen set

# a set that's immutable so you can't remove/add values

x = frozenset(["one", "two", "three", "four"])
print(x)