import random
import time

# array_one = [7, 12, 9, 11, 3]

# for i in range(0, len(array_one) - 2):
#     if array_one[i] > array_one[i + 1]:
#         array_one[i], array_one[i + 1] = array_one[i + 1], array_one[i]
#     else:
#         i += 1
#
# print(array_one)

'''
Why the Output is [7, 9, 11, 12, 3]

Let's trace the execution:

i = 0:
array_one[0] (7) > array_one[1] (12) is false.
else: i += 1 i becomes 1.
i = 1:
array_one[1] (12) > array_one[2] (9) is true.
Swap: array_one becomes [7, 9, 12, 11, 3]
i = 2:
array_one[2] (12) > array_one[3] (11) is true.
Swap: array_one becomes [7, 9, 11, 12, 3]
i = 3:
The loop terminates because i is no longer less than len(array_one) - 2.
The final 3 remains at the end because the loop only went up to the third index.
'''


'''
Corrected Code:
'''

def bubbleSort(array_one):
    for i in range(len(array_one) - 1):
        swapped = False
        for j in range(len(array_one) - i - 1):
            if array_one[j] > array_one[j + 1]:
                array_one[j], array_one[j + 1] = array_one[j + 1], array_one[j]
                swapped =True

        if not swapped:
            break


if __name__ == '__main__':
    # arr = [7, 12, 9, 11, 3]
    # arr = [3, 7, 9, 11, 12]

    array_size = 10
    print(f"--- Testing Bubble Sort with {array_size} elements ---")

    # print(f"Generating a reverse sorted array (worst case)...")
    # arr = list(range(array_size, 0, -1))

    # Average Case: Randomly shuffled (uncomment to test)
    print(f"Generating a randomly shuffled array (average case)...")
    arr = list(range(array_size))
    random.shuffle(arr)

    # Best Case: Already sorted (uncomment to test)
    # print(f"Generating an already sorted array (best case)...")
    # arr = list(range(array_size))

    print("Original Array: ", arr)
    startTime = time.perf_counter()
    bubbleSort(arr)
    endTime = time.perf_counter()
    elapsedTime = endTime - startTime
    print("Sorted Array: ", arr)

    print(f"Time taken to execute Bubble Sort Algo: {elapsedTime:.6f} seconds")


# print(array_one)