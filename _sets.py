#sets are unordered collections of unique elements
#they do not allow duplicates
#they are mutable, but the elements must be immutable
number1 = {1, 2,2, 3, 4, 5, 5, 10, 20}

number2 = {1, 2, 3, 4,4, 5, 13, 17}

print(number1)
print(number2)
print(number1.union(number2))  # Union of two sets
print(number1.intersection(number2))  # Intersection of two sets