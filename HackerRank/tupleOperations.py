
def TupOpertions():
    # https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
    number = int(input())
    tuple2=(1,2 )
    list3=[1,2]
    tuple1 = ()
    list2 = []
    list1 = (input().split(" "))
    for i in range(0, len(list1)):
        list2.append(int(list1[i]))

    tuple1 = tuple(list2)

    print(hash(tuple1))
    print(hash(tuple2))

    return