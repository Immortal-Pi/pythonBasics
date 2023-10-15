def bananaGame(string):
    # https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
    """
    :param string: long solution, not optimized
    :return:

    player1='Stuart'
    player2='Kevin'

    scoreConsonants=0
    scoreVowels=0
    substringsList=[]
    for i in range(0,len(string)):

        for j in range(i+1,len(string)+1):
            substring=string[i:j]
            # print(substring)
            exist=0
            for k in substringsList:
                if k==substring:
                    exist=1

            if exist==0:
                substringsList.append(substring)
    # print(substringsList)
    for k in substringsList:
        for i in range(0,len(string)):
            lengthcount=0
            for j in range(0,len(k)):
                if ((i + j) < len(string)):
                    if k[j]==string[i+j]:
                        lengthcount+=1
                    else:
                        break;
            if lengthcount == len(k):
                if k[0]=='a' or k[0]=='A':
                    scoreVowels+=1
                elif k[0]=='e' or k[0]=='E':
                    scoreVowels+=1
                elif k[0]=='i' or k[0]=='I':
                    scoreVowels+=1
                elif k[0]=='o' or k[0]=='O':
                    scoreVowels+=1
                elif k[0]=='u' or k[0]=='U':
                    scoreVowels+=1
                else:
                    scoreConsonants+=1

    if (scoreConsonants>scoreVowels):
        print(player1,scoreConsonants)
    elif(scoreConsonants<scoreVowels):
        print(player2,scoreVowels)
    elif(scoreConsonants==scoreVowels):
        print('Draw')
    """

    #saw this solution online
    n=len(string)
    comb=(n*(n+1)/2)
    counts=0
    countk=0

    for i in range(len(string)):
        if string[i] in "AEIOU":
            countk+=len(string[i:])
            # print(string[i:])
    if counts == countk:
        print("Draw")
    elif counts > countk:
        print("Stuart", int(counts))
    else:
        print("Kevin", int(countk))

    return