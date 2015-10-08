
import math

print 'Welcome to magic world. Choose any number between 1 - 31\n'


def magic():
    ques = {}
    print "Is your number present in this? Enter Y"
    for i in range(1, 32, 2):
        print i,

    print '\n'
    ques[0] = raw_input()


    print "\nIs your number present in this? Enter Y"
    print '2 3 6 7 10 11 14 15 18 19 22 23 26 27 30 31\n'
    ques[1] = raw_input()


    print "\nIs your number present in this? Enter Y"
    print '4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 31\n'
    ques[2] = raw_input()


    print "\nIs your number present in this? Enter Y"
    print '8 9 10 11 12 13 14 15 24 25 26 27 28 29 30 31\n'
    ques[3] = raw_input()


    print "\nIs your number present in this? Enter Y"
    for i in range(16, 32):
        print i,
    print '\n'
    ques[4] = raw_input()

    print "Aabra ka dabra........."

    for i in range(9999999):
        pass

    num = 0
    for i in ques.items():
        if i[1].lower() == 'y':
            num = num + int(math.pow(2, i[0]))

    return num


x = raw_input()
num = magic()
if num != 0:
    print "Your number is ", num
else:
    "No number selected between 1-31"

