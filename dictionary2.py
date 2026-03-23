# Creating a dictionary for Saloni
student = {
    "name": "Saloni",   # student ka naam
    "age": 17,          # age
    "course": "BCA",    # course
    "city": "Varanasi"  # city
}

# Print full dictionary
print(student)

# Access specific value
print("Name:", student["name"])

# Add new data
student["marks"] = 85

# Update data
student["age"] = 18

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)