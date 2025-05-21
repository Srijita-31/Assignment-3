numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("Even numbers in the list are:")
for num in numbers:
    if num % 2 == 0:
        print(num)
