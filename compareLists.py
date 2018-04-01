def compare(lOne, lTwo):
    if len(lOne) != len(lTwo):
        print "The lists are not the same."
        return

    for i in range(len(lOne)):
        if lOne[i] != lTwo[i]:
            print "The lists are not the same."
            return
    print "The lists are the same"
