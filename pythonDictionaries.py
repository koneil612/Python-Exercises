# phonebook_dict = {
# 'Alice': '703-493-1834',
# 'Bob': '857-384-1234',
# 'Elizabeth': '484-584-2923'
# }
# # print elizabeths phone number
# # print phonebook_dict['Elizabeth']
#
# # Add a entry to the dictionary: Kareem's number is 938-489-1234
# phonebook_dict['Kareem'] = '938-489-1234'
#
#
# # Delete Alice's phone entry.
# del phonebook_dict['Alice']
#
# # Change Bob's phone number to '968-345-2345'.
# phonebook_dict['Bob'] = '968-345-2345'
# print phonebook_dict




# # nested dictionaries::
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }
# # Write a python expression that gets the email address of Ramit.
# print ramit['email']
#
#
# # Write a python expression that gets the first of ramit's interests.
# print ramit['interests'][0]
#
# # Write a python expression that gets the email address of Jasmine.
# print ramit['friends'][0]['email']
# # Write a python expression that gets the second of Jan's two interests.
# print ramit['friends'][1]['interests'][1]

# word count exercise::
song = {}
text = open('programmers_blues.txt')
lines = text.read()
lines = lines.replace('.', '').replace('(', '').replace(')', '')
words = lines.split()
for word in words:
    word= word.upper()
    song[word] = song.get(word, 0)+1
print song

song = sorted(song.items(), key=lambda x:x[1])
print song[-10:]
