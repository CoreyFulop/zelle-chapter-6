# first_n_natural_numbers.py

def sumN(n):
    sum = 0 
    for i in range(1, n + 1):
        sum += i
    return sum

def sumNCubes(n):
    sum_cubes = 0
    for i in range(1, n + 1):
        sum_cubes += i**3
    return sum_cubes

def main():
    print("This program returns infomration about the first 'n' natural numbers.\n")

    n = eval(input("Please enter your n (natural number): "))

    sum = sumN(n)
    sum_cubes = sumNCubes(n)

    print(f"\nThe sum of the first {n} natural numbers is {sum},")
    print(f"and the sum of the cubes of the first {n} natural numbers is {sum_cubes}.")

main()