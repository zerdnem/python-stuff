number = raw_input("Enter you number: ")

    int(number)
    if len(number) != 11:
        print number + " is not 11 characters "
    else:
        print True
        print number + " is 11 characters"

