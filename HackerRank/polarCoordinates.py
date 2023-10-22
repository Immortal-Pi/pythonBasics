from cmath import phase


def polarCor():
    # https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
    number1=complex(input())
    print(abs(number1))
    print(phase(number1))



    return