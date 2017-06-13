def donations():
    totalNumberOfCans = 0
    numberOfDonations = 0
    while totalNumberOfCans <= 100:
        numberOfCans = int(input("How many cans? "))
        totalNumberOfCans += numberOfCans
        numberOfDonations += 1
    print ("Total donations: {}".format(numberOfDonations))
    print ("Total number of cans: {}".format(totalNumberOfCans))

donations()
