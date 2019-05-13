# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0 # this is so it floats
    for number in numbers:
        total += number  ##fancy way of saying total = total plus number(take the old total and add one to it and that's the new total)
                        ## total += number is exactly the same as total += total + number
    return total / length


# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))
