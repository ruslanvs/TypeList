# Takes a list and prints a message for each element in the list, based on that element's data type.

l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical', 'unicorns']

def typeCheck( checkedList ):
    listLength = len( checkedList )
    tempType = type( checkedList[0] )
    # print tempType, "tempType"
    identifiedType = ""
    sumOfStrings = ""
    sumOfNumbers = 0
    
    for i in range ( 0, listLength ):
        
        # print type(checkedList[i])
        if type( checkedList[i] ) != tempType:
            identifiedType = "The list you entered is of mixed type"
            
        elif isinstance( checkedList[i], str ):
            identifiedType = "The list you entered is of string type"

        elif isinstance( checkedList[i], int ):
            identifiedType = "The list you entered is of integer type"

        if isinstance( checkedList[i], str ):
            sumOfStrings += checkedList[i] + " "

        if not isinstance( checkedList[i], str ):
            sumOfNumbers += checkedList[i]

        tempType = type( checkedList[i] )
        
    
    if identifiedType == "The list you entered is of mixed type":
        print identifiedType
        print "String:", sumOfStrings
        print "Sum:", sumOfNumbers

    if identifiedType == "The list you entered is of string type":
        print identifiedType
        print "String:", sumOfStrings

    if identifiedType == "The list you entered is of integer type":
        print identifiedType
        print "Sum:", sumOfNumbers

typeCheck ( l1 )
typeCheck ( l2 )
typeCheck ( l3 )