# 1-10 range print loop
# for number in range(1, 11):
#     print number



#n to m (number range user inputs)
# numberStart = int(raw_input("Enter a starting number: "))
# numberEnd = int(raw_input("Enter an ending number: "))
# for number in range(numberStart, numberEnd+1):
#     print number



# print odd numbers 1-10 only
# for i in range(1, 10, 2):
#     print i



# print a square 5*5  in *'s
# size = 5
# for i in range(size):
#     print ("*" * size)



# print a square NXN square user propmts
# size = int(raw_input("How big is the square? "))
# for i in range(size):
#     print ("*" * size)

# print a box border with user input
# width = int(raw_input("What is the width? "))
# height = int(raw_input("what is the height? "))
# inner_size = width - 2
# print ('*' * width)
# for i in range(inner_size):
#     print ('*' + ' ' * inner_size + '*')
# print ('*' * width)


# print a triangle
# triangle = "*"
#     print triangle + triangle


# Multiplication Table
# digits = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for numbers in digits:
#     print str(numbers) +  " X " + str(numbers + 1)


# Bonus print a banner
text = raw_input("Enter Text here: ")
print "*" + ( "*" * len(text)) + "*"
print "*" + text + "*"
print "*" + ( "*" * len(text)) + "*"
