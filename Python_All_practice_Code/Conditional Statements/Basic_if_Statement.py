Number =int(input("Enter a Number: "))

if Number > 0:
    print(f"{Number} is a Positive Number.")
    print("This Statement is Inside The If Block.")  #If the condition is False...The if block is skipped

print("End of Program")    # This statement is outside the if block.
                           # It will always execute, whether the condition is True or False