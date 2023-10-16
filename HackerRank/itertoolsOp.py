import itertools


def itertoolsOperation():
    # https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
    # a=[[1,2,3],[2,3]]
    # b=[2,3]
    # print(list(itertools.product(*a)))
    # print(list(itertools.product(*a,b)))
    # print(list(itertools.tee(a,4)))
    #
    # list1 = [1, 2, 3]
    # list2 = [4, 5, 6]
    # combined = itertools.chain(list1, list2)
    # print(list(combined))
    #
    # numbers = [1, 2, 3, 4, 5]
    # cumulative_sum = itertools.accumulate(numbers)
    # print(list(cumulative_sum))
    #
    # numbers = [1, 2, 3, 4, 5]
    # squared = itertools.starmap(lambda x: x ** 2, [(x,) for x in numbers])
    # print(list(squared))



    # string1 = input()
    # string2 = input()
    # inputInteger1 = [int(x) for x in string1.split()]
    # inputInteger2 = [int(x) for x in string2.split()]
    #
    # output = itertools.product(inputInteger1, inputInteger2)
    # outputString = ''
    # for i in output:
    #     outputString += str(i) + ' '
    # print(outputString)





    # colors = ["red", "green", "blue"]
    # color_cycle = itertools.cycle(colors)
    # for _ in range(7):
    #     print(next(color_cycle))

    # print(list(itertools.combinations('amruth',2)))


    # permutation
    # string1=input()
    # oprations=[i for i in string1.split()]
    # # print(itertools.range(oprations,oprations[1]))
    # result=itertools.permutations(oprations[0],int(oprations[1]))
    # for i in range(int(oprations[1])):
    #     result=sorted(result,key=lambda x:x[i] )
    #     result2=sorted(result)
    #
    # stringO=''
    # for i in result2:
    #     # print(i)
    #     stringO=''
    #     for j in range(len(i)):
    #          stringO+=i[j]
    #     print(stringO)




    #combinations

    # https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
    string1=input()
    oprations=[i for i in string1.split()]
    resultList=[]
    for i in range(1,int(oprations[1])+1):
        # print(i)
        resultList.append(list(itertools.combinations(oprations[0],i)))
    # for i in range(int(oprations[1])):
    #     resultList=sorted(resultList,key=lambda x:x[i] )
    #     result2=sorted(resultList)

    # print(result2)
    print(list(resultList))






    return
