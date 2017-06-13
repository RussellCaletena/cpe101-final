def hello():
    print ('Hello!')
    userInput = input('Again (y/n)? ')
    while True:
        if (userInput == 'y'):
            print ('Hello!')
            userInput = input('Again (y/n)? ')
        else:
            print ('Goodbye!')
            break

hello()
