def mergeString(string,number):
    # https://www.hackerrank.com/challenges/merge-the-tools/problem

    splitLength=int(len(string)/number)

    stringList=[]

    for i in range(0,len(string),number):
        if (i + number)<=len(string):
            # print(string[i:i+number])
            print(removeDuplicates(string[i:i+number]))

    return

def removeDuplicates(string):
    result=set()
    resultList=[]
    for i in range(len(string)):
        if string[i] not in result:
            resultList.append(string[i])
            result.add(string[i])

    return ''.join(resultList)