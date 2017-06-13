nums = [[98, 90, 91], [46, 76, 62], [85, 90, 83], [77, 79, 81]]

def search_2D(list1, number):
    newList = []
    for row in range(len(list1)):
        for col in range(len(list1[row])):
            if list1[row][col] == number:
                newList.append((row, col))
    print (newList)

search_2D(nums, 90)
search_2D(nums, 33)
