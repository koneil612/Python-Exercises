### write an algorithm that takes a string and reverses all the characters in that string

# words = "Hello my name is Kristine. This is a long-ish string"


# print words[::-1]


# Write a function that takes in a paragraph of text and reverses each word in the paragraph1]
# para="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
#
# words = para.split()
#  # len(words)
#
# for pos in range(len(words)):
#     words_new = words[::-1]
#
# print words_new


# ***Find the kth largest
# a = [3, 2, 1, 5, 6, 4]
# k = int(raw_input("select a number for k 1-5: "))
# a.sort()
# print a
# j = a[-k]
# print j


# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# mychar = ')))((('
# open_count = 0
# closed_count = 0
# total_count = 0
# done = True
# # def counter():
#
# for char in mychar:
#   print char
#   total_count = open_count + closed_count
#   if char == '(':
#       open_count += 1
#
#   elif char == ')':
#       closed_count -= 1
#
#   total_count = open_count + closed_count
#
#   while total_count < 0:
#       done = False
#       break
#       if total_count == 0:
#           done = True
#       if total_count != 0:
#           done = False
#
# if done == True:
#    print "Valid"
# else:
#    print "Invalid"


   # damians code: for is better to use when you know how many vs while is more for something your NOT SURE
# def checkPair(s,pair="()"):
#     unclosedPair = 0
#     for c in s:
#         # counting the opens
#         if c==pair[0]:
#             unclosedPair+=1
#         # close an unclosedPair
#         if c==pair[1]:
#             unclosedPair-=1
#         if unclosedPair<0:
#             #started wtih a closing char, exit
#             return False
#     return True
#
# def checkPairs(s):
#     return checkPair(s) and checkPair(s,"{}") and checkPair(s,"[]")
#
#
# print checkPair("((alkjflkaj)))))))")

# Implement a function to convert a string to an integer.
s = '2464'

#
def converting():
    if type(s) == str:
        sti = s.split()
        change = int(sti)
        print change

converting()
