# toNumbers_function.py

def toNumbers(strList):
    for i in range(len(strList)):
        number = eval(strList[i])
        strList[i] = number

def test():
    strList1 = ["1", "2", "3"]
    print(strList1)
    toNumbers(strList1)
    print(strList1)

test()
