# name = raw_input("What is your name? ")
#
# print "Hello " + name.upper()
# print "Your name has " + str(len(name)) + " letters in it! Awesome!"

#Madlib exercise
# name = raw_input("what is your name? ")
# subject = raw_input("Please pick a school subject ")
# verb = raw_input("Please pick a verb ")
# print "Random Madlib: " + name+"'s" + " favorite subject in school was " + subject +". " + name + " found it " +verb +"."

#day of the week exercise
# day = int(raw_input("Please select a day between 0-6? "))
# if day == 0:
#     print "Sunday"
# if day == 1:
#     print "Monday"
# if day == 2:
#     print "Tuesday"
# if day == 3:
#     print "Wednesday"
# if day == 4:
#     print "Thursday"
# if day == 5:
#     print "Friday"
# if day == 6:
#     print "Saturday"

#work or sleep in excercise
# day = int(raw_input("Please select a day between 0-6? "))
# if day == 0 or day ==6:
#     print "Sleep in"
# else:
#     print "Go to work"

# Celsius to Fahrenheit
# temp = int(raw_input("Please input a temperature in Celsius: "))
# if temp == 0:
#     print "Temperature is 32 degrees Fahrenheit"
# else:
#     temp = (temp * 1.8) + 32
#     print "Temperature is now " + str(temp) + " degrees Fahrenheit"

# Tip Calculator
# bill = int(raw_input("What was your total bill amount? "))
# tipamount = raw_input("How would you rate your service 'Good', 'Fair', or 'Poor'? ")
# if tipamount == "good":
#     tipamount = tipamount.upper()
#     tipcost = bill * .20
#     print "You should tip: " + str(tipcost)
#     print "Your total bill is: " + str((bill +tipcost))
# if tipamount == "fair":
#     tipamount = tipamount.upper()
#     tipcost = bill * .15
#     print "You should tip: " + str(tipcost)
#     print "Your total bill is: " + str((bill +tipcost))
# if tipamount == "poor":
#     tipamount = tipamount.upper()
#     tipcost = bill * .10
#     print "You should tip: " + str(tipcost)
#     print "Your total bill is: " + str((bill +tipcost))

#Tip Calulator split with parties
bill = float(raw_input("What was your total bill amount? "))
tipamount = raw_input("How would you rate your service 'Good', 'Fair', or 'Poor'? ")
party = float(raw_input("How many are in your party? "))
tipamount = tipamount.upper()
if tipamount == "GOOD":
    tipcost = bill * .20
    total = float(tipcost) + bill
    print "You should tip: " + str(tipcost)
    print "Your total bill is: " + str((total))
    print "Each person should pay " + str(total / party)
if tipamount == "FAIR":
    tipcost = bill * .15
    total = float(tipcost) + bill
    print "You should tip: " + str(tipcost)
    print "Your total bill is: " + str((total))
    print "Each person should pay " + str(total / party)
if tipamount == "POOR":
    tipcost = bill * .10
    total = float(tipcost) + bill
    print "You should tip: " + str(tipcost)
    print "Your total bill is: " + str((total))
    print "Each person should pay " + str(total / party)
