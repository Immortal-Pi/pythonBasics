def triangleQst2(number):

    #https://www.hackerrank.com/challenges/triangle-quest-2/problem?isFullScreen=true
    string1='1234567890'
    string2=''
    for i in range(0,number):
        #print(((10 ** i - 1) // 9) ** 2)
        string2+=string1[i]
        # print(string2)
        reverseString=string2[::-1]
        #resultString=string2+string2[1::-1]
        # print(reverseString)
        print(string2+reverseString[1::])
    return