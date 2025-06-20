def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
numbers = [74, 35, 36, 25, 32, 24, 11, 0]
print("Original list:", numbers)
selection_sort(numbers)
print("Sorted numbers:", numbers)

    # TODO: Implement selection sort
pass
