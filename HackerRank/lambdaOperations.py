def lambdaOp():

    # list1=(1,2,3)
    #
    # # simple lambda operation (simple functions)
    # square=lambda x:x**2
    # print(square(list1[1]))
    #
    #
    # # using in maps
    # listResult=map(square,(i for i in list1))
    # listResult1=tuple(listResult)
    # print(listResult1)
    # return

    #using in sorted

    # elements = [(1, 3,-5), (2, 2, -3), (3, 1,-7)]
    # tupleElements2=sorted(elements,key=lambda x:x[1]) #useless
    # print(tupleElements2,len(tupleElements2))
    #
    # #maps
    # elements1=[2,3,4,5]
    # elements2=[5,6,7]
    # resultlist1=list(map(lambda x:x**2,elements1))
    # print(resultlist1)
    #
    # resultlist2=list(map(lambda x,y:x**2+y**2,elements1,elements2))
    # print(resultlist2)


    elements4=(1,2,3,4)
    # elements3=(3,4,5,10)
    # resultlist3=tuple(map(lambda x,y:x*y,elements4,elements3))
    # print(resultlist3)

    function1=lambda x:x*2
    result1=sorted(elements4,key=lambda x:x**2)
    print(result1)
    return