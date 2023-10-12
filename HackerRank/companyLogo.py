def companyLogo(string):
    # https://www.hackerrank.com/challenges/most-commons/problem
    stringLetters='abc'
    list1={}

    for j in range(0,len(stringLetters)):
        letterCount=0
        for i in string:

            if stringLetters[j]==i:
                #print(stringLetters[j])
                letterCount=letterCount+1
                list1[i]=letterCount
    list2=dict(sorted(list1.items(),key=lambda k:(-k[1],k[0])))
    count=1
    for k, v in list2.items():
        if (count == 4):
            break
        else:
            print(k + ' ' + str(v))
            count = count + 1
