# sum_of_squares_file.py
# Reads in a file with only spaces between the numbers on each line.

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = (nums[i])**2

def sumList(nums):
    count = 0
    for num in nums:
        count += num
    return count

def toNumbers(strList):
    for i in range(len(strList)):
        number = eval(strList[i])
        strList[i] = number

def main():
    print("This program computes the sum of squares of numbers read from a file.\n")

    infileName = input("Enter the file name: ")

    infile = open(infileName, "r")

    total = 0
    for line in infile:
        line_list = line.split()
        toNumbers(line_list)
        squareEach(line_list)
        total += sumList(line_list)

    infile.close()

    print(f"The sum of squares of all numbers in the file is {total}.")
    
main()
