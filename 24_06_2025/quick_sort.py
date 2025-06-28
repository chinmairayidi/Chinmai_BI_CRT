'''
The Quicksort algorithm takes an array of values, chooses one of the values as the 'pivot' element, and moves the other values so that 
lower values are on the left of the pivot element, and higher values are on the right of it.
O(nlogn):
O(n2):
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right =  [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
print(quick_sort([5,4,12,30,45]))