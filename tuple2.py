# Creating a tuple
numbers = (10, 20, 30, 40, 50, 20)

# Count how many times a value appears
count_20 = numbers.count(20)
print("20 appears:", count_20, "times")

# Find index of a value
index_30 = numbers.index(30)
print("Index of 30:", index_30)

# Slicing a tuple
print("Sliced tuple:", numbers[1:4])  # elements from index 1 to 3

# Check if an element exists
if 40 in numbers:
    print("40 is present in tuple")

# Tuple unpacking
a, b, c, d, e, f = numbers
print("Unpacked values:", a, b, c, d, e, f)