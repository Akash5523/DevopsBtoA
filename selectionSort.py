import random
import time


# def selectSort(test_array):
#     n = len(test_array)
#     currentVal = test_array[0]
#     for i in range(n - 1):
#         flag = False
#         for j in range(n - i - 1):
#             if test_array[j] < test_array[j + 1]:
#                 currentVal[j], test_array[j + 1] = test_array[j + 1], currentVal[j]
#                 flag = True
#         if not flag:
#             break
#

def selectSort(test_array):
    n = len(test_array)
    for i in range(n - 1):
        min_index = i
        for j in range(i+1, n):
            if test_array[j] < test_array[min_index]:
                min_index = j
        min_val = test_array.pop(min_index)
        test_array.insert(i, min_val)
        print(f"Interation {i}: ", test_array)


def selectSortUsingSwap(test_array_2):
    n = len(test_array_2)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if test_array_2[j] < test_array_2[min_index]:
                min_index = j
        test_array_2[i], test_array_2[min_index] = test_array_2[min_index], test_array_2[i]


if __name__ == '__main__':
    arr_size = 10
    arr_get = list(range(arr_size))
    random.shuffle(arr_get)
    
    print(f"Random array: {arr_get}\n")
    start_time = time.perf_counter()
    selectSort(arr_get)
    # selectSortUsingSwap(arr_get)
    end_time = time.perf_counter()
    print(f"\nSorted Array: {arr_get}")

    elapsed_time = end_time - start_time
    print(f"Total execution time: {elapsed_time:.6f} seconds")


    