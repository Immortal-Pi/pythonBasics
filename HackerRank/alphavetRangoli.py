def alpharangoli(number):
    #https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

    alphabet='abcdefghijklmnopqrstuvwxyz'
    #resultString=''
    for i in range(1,number+1):
        resultString = ''
        for j in range(1,i+1):
            if j==i:
                resultString += alphabet[number - j]
            else:
                resultString+=alphabet[number-j]+'-'

        newString=resultString[::-1]

        resultString+=newString[1::]

        print(resultString.center(number*4-3,'-'))
    for i in range(number-1,0,-1):
        resultString = ''
        count=0
        for j in range(1,i+1):

            resultString += alphabet[number-j] + '-'
        newString = resultString[::-1]

        resultString += newString[3::]

        print(resultString.center(number * 4 - 3, '-'))



    return

alpharangoli(10)