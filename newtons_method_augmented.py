# newtons_method_augmented.py

import math

def nextGuess(guess, x):
    return (guess + (x / guess))/2

def main():
    print("This program uses Newton's method to approximate a square root.\n")

    x = eval(input("Enter your number: "))

    guess = x / 2

    n = eval(input("How many times to apply Newton's method: "))

    for i in range(n):
        guess = nextGuess(guess, x)
    
    print(f"Using Newton's method, we approximate the square root of {x} as {guess}.")
    print(f"Our guess deviates from math.sqrt() by {math.sqrt(x) - guess}.")

main()
