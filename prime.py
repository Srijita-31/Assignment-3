while True:
    num = int(input("Enter a number: "))

    if num <= 1:
        print("Not a prime number.")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print("Not a prime number.")
                break
        else:
            print("It's a prime number.")

    choice = input("Do you want to try again? (yes/no): ")
    if choice.lower() != 'yes':
        break
