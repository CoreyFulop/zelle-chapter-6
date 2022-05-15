# fibonacci_augmented.py

def fibonacci(n):
    post = 1
    ante = 1
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(n - 2):
            post, ante = ante, post + ante
        return ante

def main():
    print("This program computes the nth Fibonacci number.\n")

    n = eval(input("Enter your n: "))
    fib = fibonacci(n)

    print(f"\nThe {n}th Fibonacci number is {fib}.")

main()
