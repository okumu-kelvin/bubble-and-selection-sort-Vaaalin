import numbers
from webbrowser import get



# TODO: Implement bubble sort
def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]

numbers = [74, 35, 36, 25, 32, 24, 11, 0]
print("Original list:", numbers)
bubble_sort(numbers)
print("Sorted numbers:", numbers)
pass