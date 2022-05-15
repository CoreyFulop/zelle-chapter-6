# squareEach_function.py

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = (nums[i])**2

def test():
    nums1 = [1, 2, 3, 4, 5]
    print(nums1)
    squareEach(nums1)
    print(nums1)

    print()

    nums2 = [-3, -2, -1, 0, 1, 2, 3]
    print(nums2)
    squareEach(nums2)
    print(nums2)

test()
