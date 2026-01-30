import os
import time
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Hàm sắp xếp mảng dùng Quick sort
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
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    QuickSort(arr, left, j)
    QuickSort(arr, i, right)

# Hàm sắp xếp mảng dùng Merge sort
def MergeSort(arr, left, right):
    if left >= right:
        return
    mid = (left + right) // 2

    MergeSort(arr, left, mid)
    MergeSort(arr, mid + 1, right)

    LeftPart = arr[left : mid + 1]
    RightPart = arr[mid + 1 : right + 1]

    i = j = 0
    k = left

    while i < len(LeftPart) and j < len(RightPart):
        if LeftPart[i] < RightPart[j]:
            arr[k] = LeftPart[i]
            i += 1
        else:
            arr[k] = RightPart[j]
            j += 1
        k += 1
    while i < len(LeftPart):
        arr[k] = LeftPart[i]
        i += 1
        k += 1
    while j < len(RightPart):
        arr[k] = RightPart[j]
        j += 1
        k += 1

def Heapify(arr, root, size):
    largest = root
    left = root * 2 + 1
    right = root * 2 + 2

    if left < size and arr[largest] < arr[left]:
        largest = left
    if right < size and arr[largest] < arr[right]:
        largest = right
    
    if largest != root:
        arr[largest], arr[root] = arr[root], arr[largest]
        Heapify(arr, largest, size)

# Hàm sắp xếp mảng dùng Heap sort
def HeapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        Heapify(arr, i, n)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        Heapify(arr, 0, i)

# Hàm tính thời gian thực thi code (ms)
def TimeCalculation(func, *data):
    start = time.perf_counter()
    func(*data)
    end = time.perf_counter()
    return int((end - start) * 1000)

# Duyệt qua các bộ dữ liệu và tính tốc độ các thuật toán
for i in range(10):
    with open(f"{DATA_DIR}/list{i}.txt","r") as nyann:
        n = int(nyann.readline().strip())
        unsorted_arr = list(map(float, nyann.readline().split()))
    print(f"{i}:")

    arr = unsorted_arr.copy()
    print(TimeCalculation(HeapSort, arr), "Heap sort")
    Heap_result = arr.copy()

    arr = unsorted_arr.copy()
    print(TimeCalculation(MergeSort, arr, 0, n - 1), "Merge sort")
    Merge_result = arr.copy()

    arr = unsorted_arr.copy()
    print(TimeCalculation(QuickSort, arr, 0 , n - 1), "Quick sort")
    Quick_result = arr.copy()

    start = time.perf_counter()
    Numpy_result = np.sort(unsorted_arr)
    end = time.perf_counter()
    print(int((end - start) * 1000), "sort of Numpy")

    #Kiểm tra kết quả của các hàm sort
    print("Good" if Heap_result == Merge_result == Quick_result == Numpy_result.tolist() else "Fail")
