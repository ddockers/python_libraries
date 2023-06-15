# 1 - Define a dictionary call story1, it should have the following keys:
# #"start", "middle" and "end"
story1 = {
    "start": "Illusion Girl saw the obesity epidemic was rife",
    "middle": "She realised she had the power to make healthy food items appear and taste the same as junk food",
    "end": "With her powers of illusion, Illusion Girl helped the population live longer, healthier lives"
}
 # 2 - Print the entire dictionary
print(story1)

# 3 - Print the type of your dictionary
print(type(story1))

#4 - Print only the keys
print(story1.keys())

#5 - Print only the values
print(story1.values())

# 6 - Print the individual values using the keys (individually, lots of print commands)
print(story1["start"])
print(story1["middle"])
print(story1["end"])

# 7 - Now let's add a new key:value pair.
story1["hero"]= "Illusion Girl"
print(story1)