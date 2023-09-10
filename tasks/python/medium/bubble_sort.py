# Python - Medium

def bubble_sort(arr):
    for l in range(0, len(arr)):
        for m in range(l+ 1, len(arr)):
            if arr[l] >= arr[m]:
                arr[l], arr[m] = arr[m], arr[l]

arr = [64, 25, 12, 22, 11]
print("Original array:", arr)

bubble_sort(arr)
print("Sorted array:", arr)
