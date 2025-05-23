def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
numbers = list(map(int, input("Enter integers separated by space: ").split()))
bubble_sort(numbers)
print("Sorted list:", numbers)
# 0   1  2 3  4
# 70 12 65 30 18
# 12 70 65 30 18
# 12 65 70 30 18
# 12 65 30 70 18
# 12 65 30 18 70

# 12 65 30 18 70

# 12 30 65 18 70
# 12 30 18 65 70