arr = [17, 10, 3, 19, 8, 12, 1, 0]

minVal = arr[0]
for ele in range(len(arr)):
    if arr[ele] < minVal:
        minVal = arr[ele]


print("Min Value is: ", minVal)