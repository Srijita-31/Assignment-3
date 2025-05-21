def linear_search(list, target):
    for index in range(len(list)):
        if list[index] == target:
            return index  
    return -1  
numbers = list(map(int, input("Enter list elements separated by space: ").split()))
target = int(input("Enter the element to search: "))

result = linear_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
