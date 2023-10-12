def stringFormat():
    # https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
    number=int(input())
    for i in range(1,number+1):
        #print(f'{oct(i)[2:]}')
        print(f'{i}'.rjust(len(f'{bin(number)[2:]}'))+' '+ f'{oct(i)[2:]}'.rjust(len(f'{bin(number)[2:]}'))+' '+f'{hex(i).upper()[2:] }'.rjust(len(f'{bin(number)[2:]}'))+' ' +f'{bin(i)[2:]}'.rjust(len(f'{bin(number)[2:]}')))