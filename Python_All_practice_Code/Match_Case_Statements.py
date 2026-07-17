Number=int(input("Enter a Number Between 1-7"))
match Number:
    case 1:print("Monday")
    case 2:print("Tuesday")
    case 3:print("Wednsday")
    case 4:print("Thrusday")
    case 5:print("Friday")
    case 6:print("Saturday")
    case 7:print("Sunday")
    case _:print("Enter Number Betweeen 1-7")   #Defult Match_Case


Mark=int(input("Enter a Mark"))
match Mark:
    case x if x<=100 and x>=80:print("A")
    case y if y<=79 and y>=60:print("B")
    case Z if Z<=59 and Z>=35:print("C")
    case _ :print("Fail")