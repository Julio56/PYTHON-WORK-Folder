# using online "Reading CSV Files in Python - https://www.youtube.com/watch?v=efSjcrp87OY"
# trying to figure out the way to read the csv and then sum up the fields (months and then data)

# import csv

# with open('../RUTJC201904DATA3/hw/week3/Instructions/PyBank/Resources/budget_data.csv') as file:
#     R = csv.reader(file)

#     count = 0

# for row in csv.reader(file):
# print(col # for troubleshooting)
# for col in row[1]:
#       total += int(col)
#   print total

#        count += 1

#############################################################

# with open('../RUTJC201904DATA3/hw/week3/Instructions/PyBank/Resources/budget_data.csv') as file:
#     headerline = file.next()
#     total = 0
#     for row in file:
#         total += int(row[1])
# print(total)
############################################################

# print("hello computer")
# b = 109
# print(b)
# csv = b + 100
# print(csv)

# e = 10
# f = 8
# if e < f:
#     print("e is less than f")
# elif e == f:
#     print("e is equal to f")
# else:
#     print("e is greater than f")


name = "Joe"
height_m = 2
weight_kg = 110
bmi = weight_kg / (height_m ** 2)
print("bmi: ")
print(bmi)
if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")

b = ["banana", "apple", "microsoft"]
print (b)
temp = b[0]
b[0] = b[2]
b[2] = temp
print (b)

# using lists
print(list(range(1, 100)))
total = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)




