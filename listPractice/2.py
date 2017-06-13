lines = ['Hello there.',
         'How now brown cow?',
         'I like cheese']
def line_counts(list1, character):
    newList = []
    count = 0
    i = 0
    while i < len(list1):
        if character in list1[i]:
            count += 1
            newList.append(count)
        i += 1
    print (newList)

line_counts(lines, 'o')
