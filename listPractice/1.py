list1 = [2, 7, 1, 4]
list2 = [6, -1]
def shuffle(list1, list2):
    newList = []
    len1 = len(list1)
    len2 = len(list2)
    for i in range(max(len1, len2)):
        if i < len1:
            newList.append(list1[i])
        if i < len2:
            newList.append(list2[i])
    print (newList)

shuffle(list1, list2)
