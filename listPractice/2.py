lines = ['Hello there.',
         'How now brown cow?',
         'I like cheese']

def line_counts(list1, character):
    newList = []
    i = 0
    while i < len(list1):
        number = characterCount(list1[i], character)
        newList.append(number)
        i += 1
    print (newList)

def characterCount(string ,character):
    charCount = 0
    for i in range(len(string)):
        if string[i] == character:
            charCount += 1
    return charCount

line_counts(lines, 'o')
