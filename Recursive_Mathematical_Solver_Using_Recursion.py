def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    print("\\n--- RECURSIVE MATHEMATICAL SOLVER ---")
    print("1. Factorial")
    print("2. Fibonacci series")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            print("Factorial =", factorial(n))
    elif choice == "2":
        terms = int(input("Enter number of terms: "))
        if terms <= 0:
            print("Please enter a positive number of terms.")
        else:
            for i in range(terms):
                print(fibonacci(i), end=" ")
            print()
    elif choice == "3":
        print("Exiting solver. Thank you!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")