import time
from array import array
import random
from sys import flags
from turtledemo.penrose import start


def bubbleSort(test_array):
    n = len(test_array)
    for i in range(n - 1):
        swapped = False
        for j in range(n-i-1):
            if test_array[j] > test_array[j + 1]:
                test_array[j], test_array[j + 1] = test_array[j + 1], test_array[j]
                swapped = True

        if not swapped:
            break


def bubbleSortDesc(desc_array):
    m = len(desc_array)
    for x in range(m - 1):
        flag = False
        for y in range(m - x -1):
            if desc_array[y] < desc_array[y + 1]:
                desc_array[y], desc_array[y + 1] = desc_array[y + 1], desc_array[y]
                flag = True
        if not flag:
            break


if __name__ == '__main__':
    arr_size = 20
    # Average case, Time Complexity:
    arr_get = list(range(arr_size))
    random.shuffle(arr_get)
    
    print(f"Random Array List: {arr_get}")
    start_time = time.perf_counter()
    bubbleSort(arr_get)
    end_time = time.perf_counter()
    print(f"Sorted Array Ascending: {arr_get}")
    elapsed_time = end_time - start_time
    print(f"Time take to execute this code in ascending order: {elapsed_time:.6f} seconds.\n")

    print(f"Get ascending order array: {arr_get}")
    desc_start_time = time.perf_counter()
    bubbleSortDesc(arr_get)
    desc_end_time = time.perf_counter()
    print(f"Sorted Array Descending: {arr_get}")
    '''
    Worst case time complexity O(n^2).
    '''
    elapsed_desc_time = desc_end_time - desc_start_time
    print(f"Time take to execute this code in descending order: {elapsed_desc_time:.6f} seconds.")







