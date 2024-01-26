
import numpy as np

if __name__ == '__main__':

    a = np.array(
        [
            [1,2,3,4,5],
            [6,7,8,9,10],
            [7,8,5,4,2]
        ],dtype=int
    )
    b=np.array(
        [
            [5,4,3,2,1],
            [10,9,8,6,5],
            [1,2,3,4,5]
        ],dtype=int
    )
    # a=a.reshape(5,3,1)
    # print(a)

    # print(a.flatten())
    #
    # print(a.transpose())
    #
    # print(np.concatenate((b,a),axis=0))
    #
    # print(np.stack((a,b),axis=0))
    #
    # print(np.split(a,3))
    # print(np.hsplit(a,5))
    # print(np.vsplit(a,1))

    c=[3,4,5,2,1]

    # a=np.append(a,[c],axis=0)
    # print(a)


    #object is individual rows
    # a=np.insert(a,3,b,axis=0)
    # print(a)

    c=np.insert([c],1,a,axis=0)
    print(c)
