while True:
    s = input("Enter a string: ")
    s=s.lower()
    if s == s[::-1]:
        print("It's a palindrome.")
    else:
        print("It's not a palindrome.")
    
    choice = input("Do you want to try again? (yes/no): ")
    if choice.lower() != 'yes':
        break
