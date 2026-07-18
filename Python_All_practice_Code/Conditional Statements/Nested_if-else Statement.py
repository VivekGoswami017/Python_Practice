Marks=int(input("Enter Mark :"))
if Marks>0:
    if Marks<=100 and Marks>=80:
          print("Grade A")
    elif Marks<=79 and Marks>=60:
          print("Grade B")
    elif Marks<=59 and Marks>=45:
         print("Gread C")
    else:
       print("Fail")

else:
    print("Negative Marking is Invalid...")