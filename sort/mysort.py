import os
import time
import numpy as np
from numba import njit # dùng để biên dịch sang mã máy để tăng tốc độ

# Đường dẫn đến data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

@njit
def QuickSort(arr, left, right):
    if left >= right:
        return
    pivot = arr[(left + right) // 2]
    i, j = left, right
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
            j -= 1
    QuickSort(arr, left, j)
    QuickSort(arr, i, right)

@njit
def MergeSort(arr, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    MergeSort(arr, left, mid)
    MergeSort(arr, mid + 1, right)
    left_part = arr[left:mid + 1].copy()
    right_part = arr[mid + 1:right + 1].copy()
    i = j = 0
    k = left
    while i < left_part.size and j < right_part.size:
        if left_part[i] < right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    while i < left_part.size:
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < right_part.size:
        arr[k] = right_part[j]
        j += 1
        k += 1

@njit
def Heapify(arr, root, size):
    largest = root
    left = root * 2 + 1
    right = root * 2 + 2
    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != root:
        tmp = arr[root]
        arr[root] = arr[largest]
        arr[largest] = tmp
        Heapify(arr, largest, size)

@njit
def HeapSort(arr):
    n = arr.size
    for i in range(n // 2 - 1, -1, -1):
        Heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        tmp = arr[0]
        arr[0] = arr[i]
        arr[i] = tmp
        Heapify(arr, 0, i)
# Đo thời gian code
def TimeCalculation(func, *data):
    start = time.perf_counter()
    func(*data)
    end = time.perf_counter()
    return int((end - start) * 1000)

for i in range(10):
    with open(f"{DATA_DIR}/list{i}.txt", "r") as nyann:
        n = int(nyann.readline().strip())
        unsorted_arr = np.fromstring(nyann.readline(), sep=" ", dtype=np.float64)

    print(f"{i}:")

    arr = unsorted_arr.copy()
    print(TimeCalculation(HeapSort, arr), "Heap sort")
    heap_result = arr.copy()

    arr = unsorted_arr.copy()
    print(TimeCalculation(MergeSort, arr, 0, n - 1), "Merge sort")
    merge_result = arr.copy()

    arr = unsorted_arr.copy()
    print(TimeCalculation(QuickSort, arr, 0, n - 1), "Quick sort")
    quick_result = arr.copy()

    start = time.perf_counter()
    numpy_result = np.sort(unsorted_arr)
    end = time.perf_counter()
    print(int((end - start) * 1000), "sort of Numpy")

    # Kiểm tra lại xem các hàm sort đúng hay sai
    print("Good" if np.array_equal(heap_result, merge_result)
          and np.array_equal(merge_result, quick_result)
          and np.array_equal(quick_result, numpy_result)
          else "Fail")
