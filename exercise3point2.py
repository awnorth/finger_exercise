#  Intro to computation and Programming using Python - Finger Exercise 3.2
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
