# This is a sample Python script.
import missing_ranges

'''
n is number of elements in array
arr is the sorted array
lower is the lower range
upper is the upper range
'''
arr = []

# number of elements as input
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input("Enter element:"))

    arr.append(ele)

# taking lowe range
lower = input("Enter Lower Range:")

# taking upper range
upper = input("Enter Upper Range:")

# calling missing range funtion
result = missing_ranges.missingRanges(nums=arr, l=int(lower), u=int(upper))

print("Missing Ranges:", result)  # printing missing ranges
