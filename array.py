my_array = [12,7,8,9,10]
print(my_array[0])

minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print("Lowest Value:", minVal)