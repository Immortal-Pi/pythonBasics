import itertools


def itertoolsOperation():
    # https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
    a=[[1,2,3],[2,3]]
    b=[2,3]
    print(list(itertools.product(*a)))
    print(list(itertools.product(*a,b)))
    print(list(itertools.tee(a,4)))

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = itertools.chain(list1, list2)
    print(list(combined))

    numbers = [1, 2, 3, 4, 5]
    cumulative_sum = itertools.accumulate(numbers)
    print(list(cumulative_sum))

    numbers = [1, 2, 3, 4, 5]
    squared = itertools.starmap(lambda x: x ** 2, [(x,) for x in numbers])
    print(list(squared))




    return
