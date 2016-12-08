from sys import argv

script, filename = argv

text = open('haiku.txt')
num_lines = sum(1 for line in text)
print num_lines
