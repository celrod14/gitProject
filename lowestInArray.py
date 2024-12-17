myArray = [4,3,2,1,6,5,-9]

# lowest = myArray[0]

# for i in myArray:
#     if(i < lowest):
#         lowest = i

# print(lowest)

# qaCreate a variable 'minVal' and set it equal to the first value of the array.
# Go through every element in the array.
# If the current element has a lower value than 'minVal', update 'minVal' to this value.
# After looking at all the elements in the array, the 'minVal' variable now contains the lowest value.

minVal = myArray[0]
for elements in myArray:
    if elements < minVal:
        minVal = elements
print (elements)