#  Intro to computation and Programming using Python - Finger Exercise 3.2
# Let s be a string that contains a sequence of decimal humbers separated by commas, e.g., s '1.23,2.4,3.123'.
# Write a program that prints the sum of the numbers in s.
h = '88.6,764.3'
num = ''
total = 0

for count, x in enumerate(h):
    if x == ',' or count == len(h)-1:
        total += float(num)
        num = ''
    else:
        num += x
print 'The sum of h is ',total
