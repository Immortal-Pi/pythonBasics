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

    # SET FUNCTIONS

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
    # firstNumber=int(input())
    # setList=set(map(int,input().split()))
    # secondNumber=int(input())
    # setList2=set(map(int,input().split()))
    # print(len(setList.union(setList2)))





    # https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

    # SET MUTATIONS
    # s=set("Hacker")
    # print(s)
    # s.update("RANK")
    # print(s)
    # elementsNumber=int(input())
    # set1=set(map(int,input().split()))
    # elementsOperation=int(input())
    # OperationCommands=[]
    # elementsCommand=[]
    # for i in range(0,elementsOperation):
    #     OperationCommands.append(input().split())
    #     elementsCommand.append(set(map(int,input().split())))
    # # print(OperationCommands)
    # # print(elementsCommand)
    #
    # for index,i in enumerate(OperationCommands):
    #     if i[0]=='intersection_update':
    #
    #         set1.intersection_update(elementsCommand[index])
    #     elif i[0]=='update':
    #         # for j in range(int(i[1])):
    #         set1.update(elementsCommand[index])
    #
    #     elif i[0]=='symmetric_difference_update':
    #         # for j in range(int(i[1])):
    #         set1.symmetric_difference_update(elementsCommand[index])
    #     elif i[0]=='difference_update':
    #         # for j in range(int(i[1])):
    #         set1.difference_update(elementsCommand[index])
    #     # print(set1,i[0])
    # sum=0
    # for i in set1:
    #     sum+=i
    #
    # print(sum)



    # https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

    # number=int(input())
    # numberList=list(map(int,input().split()))
    # # print(list(numberList))
    # for i in numberList:
    #     if numberList.count(i) ==1:
    #
    #         print(i)
    #







    #https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

    # testCases=int(input())
    # for i in range(testCases):
    #     setANumber=int(input())
    #     setAelements=set(map(int,input().split()))
    #     setBNumber = int(input())
    #     setBelements = set(map(int, input().split()))
    #     print(setAelements.issubset(setBelements))
    #     set


    # https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true


    setAelements = set(map(int, input().split()))
    booleanAnswer=bool
    testCases = int(input())
    for i in range(testCases):


        setBelements = set(map(int, input().split()))
        booleanAnswer=booleanAnswer and setAelements.issuperset(setBelements) and len(setAelements) > len(setBelements)
        print(booleanAnswer)
    print(booleanAnswer)
    return