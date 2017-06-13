def squares():
    last = 3
    i = 0
    sumOfSquares = 0
    while i <= last:
        square = i**2
        print ('The number {} squared is {}.'.format(i, square))
        sumOfSquares += square
        i += 1
    print ('The sum of the squares is {}'.format(sumOfSquares))

squares()
