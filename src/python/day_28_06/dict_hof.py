from functools import reduce

# Sample dictionary
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Higher-order function using map to double each value
doubled_numbers = dict(map(lambda item: (item[0], item[1] * 2), numbers.items()))
print("Doubled numbers:", doubled_numbers)

# Higher-order function using filter to keep only even values
even_numbers = dict(filter(lambda item: item[1] % 2 == 0, numbers.items()))
print("Even numbers:", even_numbers)

# Higher-order function using reduce to find the sum of all values
sum_of_numbers = reduce(lambda x, y: x + y[1], numbers.items(), 0)
print("Sum of numbers:", sum_of_numbers)
