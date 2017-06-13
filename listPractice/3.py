nums = [[98, 90, 91], [46, 76, 62], [85, 90, 83], [77, 79, 81]]

def sum_list(list1):
    total = 0
    for item in list1:
        total += item
    return total

def sum_2D(nums):
    i = 0
    total = 0
    while i < len(nums):
        total += sum_list(nums[i])
        i += 1
    print (total)

sum_2D(nums)
