def setsOp():

    # https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

    # number = int(input())
    # set1 = set()
    # list1 = []
    # for i in range(number):
    #     set1.add(input())
    #
    # print(len(set1))

    # s1=map(int, input().split())
    # s=set('amruthpai')
    # s.add('H')
    # print(s,list(s1))





    # https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
    # integerNumbers = int(input())
    # set1=set(map(int,input().split()))
    # print(set1)
    # commandNumbers=int(input())
    # commands=[]
    # for i in range(commandNumbers):
    #     commands.append(input().split())
    # # print(commands)
    #
    # for i in commands:
    #     if i[0]=='pop':
    #         set1.pop()
    #     elif i[0]=='remove':
    #         set1.remove(int(i[1]))
    #     elif i[0]=='discard':
    #         set1.discard(int(i[1]))
    # sum=0
    # for i in set1:
    #     sum+=i
    # print(sum)






    # https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true

    # UNION OPERATION

    # s=set("Hacker")
    # print(s)
    # s=s.union([1,2,3,4])
    # s=s|set("5678")
    # s=s.union({"Z":1})
    # s=s|set("AMruth")
    # print(s)


    firstNumber=int(input())
    setList=set(map(int,input().split()))

    secondNumber=int(input())
    setList2=set(map(int,input().split()))

    print(len(setList.union(setList2)))

    return