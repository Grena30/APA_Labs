import math
import random
import time

from prettytable import PrettyTable
from matplotlib import pyplot as plt
from merge_sort import merge_sort as ms
from quick_sort import quick_sort as qs
from heap_sort import heap_sort as hs
from counting_sort import counting_sort as cs


if __name__ == '__main__':

    random.seed(15)

    n = 100000
    start = 0
    end = 10000
    div = 20
    image_num = 1
    digit_num = 3

    arr = [random.randint(start, end) for i in range(n)]
    arr_indexes = [math.floor((i + 1) * n / div) for i in range(div)]
    time_results = list()

    # Quick Sort

    current_results = list()
    qs_arrays = list()

    for i in arr_indexes:
        start_time = time.perf_counter()
        qs(arr[:i+1])
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        current_results.append(round(elapsed_time, digit_num))

    time_results.append(current_results)

    plt.figure(image_num)
    plt.plot(arr_indexes, time_results[0], label='Quick Sort', color='blue')
    plt.xlabel('Number of elements sorted')
    plt.ylabel('Elapsed time, s')
    plt.title('Quick Sort')
    plt.legend()
    image_num += 1

    # Merge Sort

    current_results = list()
    ms_arrays = list()

    for i in arr_indexes:
        start_time = time.perf_counter()
        ms(arr[:i+1])
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        current_results.append(round(elapsed_time, digit_num))

    time_results.append(current_results)

    plt.figure(image_num)
    plt.plot(arr_indexes, time_results[1], label='Merge Sort', color='blue')
    plt.xlabel('Number of elements sorted')
    plt.ylabel('Elapsed time, s')
    plt.title('Merge Sort')
    plt.legend()
    image_num += 1

    # Heap Sort

    current_results = list()
    hs_arrays = list()

    for i in arr_indexes:
        start_time = time.perf_counter()
        hs(arr[:i+1])
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        current_results.append(round(elapsed_time, digit_num))

    time_results.append(current_results)

    plt.figure(image_num)
    plt.plot(arr_indexes, time_results[2], label='Heap Sort', color='blue')
    plt.xlabel('Number of elements sorted')
    plt.ylabel('Elapsed time, s')
    plt.title('Heap Sort')
    plt.legend()
    image_num += 1

    # Counting Sort

    current_results = list()
    cs_arrays = list()

    for i in arr_indexes:
        start_time = time.perf_counter()
        cs(arr[:i + 1])
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        current_results.append(round(elapsed_time, digit_num))

    time_results.append(current_results)

    plt.figure(image_num)
    plt.plot(arr_indexes, time_results[3], label='Counting Sort', color='blue')
    plt.xlabel('Number of elements sorted')
    plt.ylabel('Elapsed time, s')
    plt.title('Counting Sort')
    plt.legend()
    image_num += 1

    # Time results

    myTable = PrettyTable(arr_indexes)
    myTable.add_row(time_results[0])
    myTable.add_row(time_results[1])
    myTable.add_row(time_results[2])
    myTable.add_row(time_results[3])

    print("Quick Sort")
    print(myTable[0])

    print("Merge Sort")
    print(myTable[1])

    print("Heap Sort")
    print(myTable[2])

    print("Counting Sort")
    print(myTable[3])

    # All the graphs

    plt.figure(image_num)
    plt.plot(arr_indexes, time_results[0], label='Quick Sort', color='black')
    plt.plot(arr_indexes, time_results[1], label='Merge Sort', color='cyan')
    plt.plot(arr_indexes, time_results[2], label='Heap Sort', color='green')
    plt.plot(arr_indexes, time_results[3], label='Counting Sort', color='blue')
    plt.xlabel('Number of elements sorted')
    plt.ylabel('Elapsed time, s')
    plt.title('Sorting Algorithms')
    plt.legend()
    plt.show()
    
