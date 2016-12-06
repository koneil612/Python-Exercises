# this is the code for the hard number ((picking the number myself)):
# secret_number = 5
# print "I am thinking of a number between 1 and 10."
# guess = int(raw_input("Pick a number bewteen 1 and 10 "))
# while guess <> secret_number:
#      print "Nope, try again!"
#      guess = int(raw_input("Pick a number bewteen 1 and 10 "))
# print "Yes!! You win"


# this is pulling with a hard number but staying if it's too high or low.
# secret_number = 5
# print "I am thinking of a number between 1 and 10."
# guess = int(raw_input("Pick a number bewteen 1 and 10 "))
# while guess <> secret_number:
#     if guess < secret_number:
#         print str(guess) + " is too low, try again"
#     if guess > secret_number:
#         print str(guess) + " is too high, try again"
#     guess = int(raw_input("Pick a number bewteen 1 and 10 "))
# print "Yes!! You win"

# random number generator
# from random import randint;
# guess = randint(1,10)
# user_guess = int(raw_input("Pick a number between 1 and 10 "))
# while user_guess <> guess:
#     print "Nope, try again!"
#     user_guess =int(raw_input("Pick a number between 1 and 10 "))
# print "Yes! You win :) "

# random number generator with ELIF showing high or low
# from random import randint;
# guess = randint(1,10)
# user_guess = int(raw_input("Pick a number between 1 and 10 "))
# while user_guess <> guess:
#     if user_guess < guess:
#         print str(user_guess) + " is too low, try again"
#     elif user_guess > guess:
#         print str(user_guess) + " is too high, try again"
#     user_guess =int(raw_input("Pick a number between 1 and 10 "))
# print "Yes! You win :) "


# random number generator with a limit of guesses
from random import randint;
guess = randint(1,10)
remaining = 5
print "I'm thinking of a number between 1 and 10"
print "You have " + str(remaining) + " guesses left";
user_guess = int(raw_input("Pick a number between 1 and 10 "))
while user_guess <> guess and remaining >= 1:
    remaining = remaining - 1
    print "Nope, try again."
    print "You have " + str(remaining) + " guesses left."
    user_guess = int(raw_input("Pick a number between 1 and 10 "))
    if remaining == 0:
        print "You ran out of guesses. You lost :( "
print "Yes! You win :) "
