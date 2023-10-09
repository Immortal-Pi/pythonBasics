import math
def patternPyramid(number):

    # https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true

    for i in range(number):
        print(('H' * i).rjust(number - 1) + 'H' + ('H' * i).ljust(number - 1))

    for i in range (0,number+1):
        print(('H'*number).center(number*2,' ')+('H'*number).center(number*6))

    for i in range(0,(number+1)//2):
        print(('H' * number * 5).center(number * 6))

    for i in range (0,number+1):
        print(('H'*number).center(number*2,' ')+('H'* number).center(number*6))

    for i in range(number):
        print((('H' * (number - i - 1)).rjust(number) + 'H' + ('H' * (number - i - 1)).ljust(number)).rjust(number * 6))


def stringPatter(givenString, max_width):
    # https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
    #result = [givenString[i:i + max_width] for i in range(0, len(givenString), max_width)]
    text=[]
    for i in range(0,len(givenString),max_width):
        text.append(givenString[i:i+max_width])

    string1=''
    for i in text:
        string1=string1 + i + '\n'
    print(string1)
    print(len(string1))
    return

def matPattern(length,width):
    design1='.|.'
    design2='-'
    design3='WELCOME'
    print((math.floor(7/2)))
    for i in range(0,math.floor(length/2)):
        print((design1*(1+i*2)).center(width,'-'))
    print((design3).center(width,'-'))
    for i in range(0,math.floor(length/2)):
        print((design1*(length-1-(1+i*2))).center(width,'-'))

