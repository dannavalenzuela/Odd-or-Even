# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# Extra:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

repeat = "Y"

while repeat == "Y":
    
    num = int(raw_input("Enter a dividend number: "))
    check = int(raw_input("Enter a divisor number: "))
    
    decide = num % 2
    
    
    if num % 4 == 0:
        print "%d is an EVEN number and is divisble by 4" % num
    elif num % 2 == 0:
        print "%d is EVEN" % num
    else:
        print "%d is ODD" % num
    
    
    answer = num % check
    
    if answer == 0:
        print "Your divisor of %d divides evenly into %d" % (check, num)
    else:
        print "Your divisor of %d does NOT divide evenly into %d" % (check, num)
    
    repeat = str(raw_input("Do you want to try again? Y or N: "))
    repeat = repeat.upper()

print "Good-bye!"