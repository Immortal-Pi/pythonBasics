def setManipulation():
    number1=int(input())
    string1=input()
    resultset1 = set()
    resultset2 = set()
    set1 = set(map(int,string1.split()))
    number2 = int(input())
    string2 = input()
    set2 = set(map(int, string2.split()))

    print(set1)
    resultset1.update(set1.difference(set2))

    for i in resultset1:
        print(i)
    resultset2.update(set2.difference(set1))
    for i in resultset2:
        print(i)

    # sorted(resultset)
    # print(resultset)



    return