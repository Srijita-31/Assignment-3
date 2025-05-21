def pascals_triangle(n):
    for i in range(n):
        print(' ' * (n - i), end='')
        val = 1
        for j in range(i + 1):
            print(val, end=' ')
            val = val * (i - j) // (j + 1)
        print()  
rows = int(input("Enter the number of rows: "))
pascals_triangle(rows)
