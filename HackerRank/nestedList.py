def NestedList():
    # https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
    lowest = 9999;
    secondLowest = 9999;

    list1 = list(list())

    for _ in range(int(input())):
        list2 = list()
        name = input()
        score = float(input())

        list2.append(name)
        list2.append(score)
        list1.append(list2)


    list1.sort()
    print (list1)

    for i in range(len(list1)):
        if list1[i][1] < lowest:
            secondLowest = lowest
            lowest = list1[i][1]

    print (lowest,secondLowest)

    for i in range(0,len(list1)):
        if list1[i][1] < secondLowest and list1[i][1] > lowest:
            secondLowest = list1[i][1]

    for i in list1:
        if (i[1] == secondLowest):
            print(i[0])