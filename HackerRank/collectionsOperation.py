import calendar
import collections


def collectionsOp():
    # https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
    # counter
    # lis1t=list(map(int,input().split()))
    # print(lis1t)
    # print(collections.Counter(lis1t))
    # print(collections.Counter(lis1t).items())
    # print(collections.Counter(lis1t).keys())
    # print(collections.Counter(lis1t).values())
    # print(collections.Counter(lis1t).values())


    # length1=int(input())
    # list1=collections.Counter(list(map(int,input().split())))
    # print(type(list1))
    # custno=int(input())
    # totalCash=0
    # print(list1)
    #
    # for i in range(custno):
    #     cust=list(map(int,input().split()))
    #     # print(cust[0])
    #     # print(list1.keys())
    #     if cust[0] in list1.keys() and list1[cust[0]]>0:
    #         totalCash+=cust[1]
    #         # print(list1[cust[0]])
    #         # list1.update({cust[0]:list1[custno]-=1})
    #         list1[cust[0]]-=1
    #     #     print(list1[cust[0]])
    #     # print(list1.items(),totalCash)
    # print(totalCash)






    # https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
    # default dict
    # list=[1,2,3,4]
    # d=collections.defaultdict(list)
    # d[1].append(2)
    # d[1].append(3)
    # d['python'].append("not relevant ")
    # print(d)
    # listinput=list(map(int,input().split()))
    # defaultDict=collections.defaultdict(list)
    # for i in range(listinput[0]):
    #     defaultDict[input()].append(i+1)
    # # print(defaultDict)
    # for i in range(listinput[1]):
    #     charInput=input()
    #     charOutput=''
    #     if charInput in defaultDict.keys():
    #         for i in range(len(defaultDict[charInput])):
    #             charOutput+=str(defaultDict[charInput][i])+' '
    #         print(charOutput)
    #     else:
    #         print(-1)





    # https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
    # namedtuple
    # car=collections.namedtuple('Car','Price Mileage Color Class')
    # xyz=car(Price=20000,Mileage=30,Color='blue',Class='Y')
    # print(xyz)


    # studentNumbers=int(input())
    # defaultdict1=collections.defaultdict(list)
    # totalMarks=0
    # orderlist=input()
    # print(orderlist)
    # student = collections.namedtuple('Student', orderlist)
    # # xyz=student('2','23','abc','amruth')
    # # print(xyz)
    # for i in range(studentNumbers):
    #     list1=input().split()
    #
    #     xyz=student(list1[0],list1[1],list1[2],list1[3])
    #     defaultdict1['Student'].append(xyz)
    #     totalMarks+=int(xyz.MARKS)
    # print(f'{totalMarks/studentNumbers:.2f}')
    # print(defaultdict1)







    # https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
    # orderedDict

    # ordinary_dictionary={}
    # ordinary_dictionary=collections.OrderedDict()
    # ordinary_dictionary['a']=1
    # ordinary_dictionary['b'] = 2
    # ordinary_dictionary['c']=3
    # ordinary_dictionary['a']+=4


    # numberofItems=int(input())
    # ordinary_dictionary={}
    # for i in range(numberofItems):
    #     listItems=list(input().split())
    #     itemString=''
    #     for i in listItems:
    #         if not i.isdigit():
    #             itemString+=' '+i
    #     itemString=itemString.strip()
    #     if itemString not in ordinary_dictionary.keys():
    #         ordinary_dictionary[itemString]=int(listItems[len(listItems)-1])
    #     else:
    #         ordinary_dictionary[itemString]+=int(listItems[len(listItems)-1])
    # for k,v in ordinary_dictionary.items():
    #     print(k,v)





    #https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
    # word order
    # inputNumber=int(input())
    # ordinary_dictionary={}
    # for i in range(inputNumber):
    #     string1=input()
    #     if string1 in ordinary_dictionary.keys():
    #         ordinary_dictionary[string1]+=1
    #     else:
    #         ordinary_dictionary[string1]=1
    # print(len((ordinary_dictionary)))
    # string2=''
    # for i in ordinary_dictionary.values():
    #     string2+=str(i)+' '
    # string2=string2.strip()
    # print(string2)



    # https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
    # deque
    doubleEndedQueue=collections.deque()
    number=int(input())
    for i in range(number):
        stringOperation=list(input().split())
        if stringOperation[0]=='append':
            doubleEndedQueue.append(int(stringOperation[1]))
        elif stringOperation[0]=='appendleft':
            doubleEndedQueue.appendleft(int(stringOperation[1]))
        elif stringOperation[0]=='pop':
            doubleEndedQueue.pop()
        elif stringOperation[0]=='popleft':
            doubleEndedQueue.popleft()
    stringAnswer=''
    for i in doubleEndedQueue:
        stringAnswer+=str(i)+' '
    stringAnswer=stringAnswer.strip()
    print(stringAnswer)

    return