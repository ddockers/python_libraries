# Dictionaries

# key-value pairs

# Key is the name/reference, value is the data stored

# Making a dictionary

student_1 = {
    "name": "Deanne",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "git", "data_types", "collections"] # a list within a dict
}
print(type(student_1))
print(student_1)

# How to access parts of the dict

print(student_1["stream"])
print(student_1["completed_lesson_names"][0])
print(student_1["completed_lesson_names"][1:3])

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"])