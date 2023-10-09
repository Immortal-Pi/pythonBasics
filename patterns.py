def patternPyramid(number):

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

