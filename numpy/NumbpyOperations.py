import numpy as np



if __name__=='__main__':

    # [1,2,4,5] #python list
    #numpy arrays

    a=np.array([1,2,3,4,5,6])
    b=np.array([5,6,7,8,9,10])
    # print(a[0],b[1])

    c=np.array([
        [1,3,4],
        [4,5,6],
        [7,8,9]

    ])
    # print(c)

    a1=[1,2,3,4]
    b1=[5,6,7,8]
    # print(a1+b1)

    # numpy considers this as 2 4d vectors
    a1 = np.array([1, 2, 3, 4])
    b1 = np.array([5, 6, 7, 8])
    # print(a1 + b1)


    #fill up an array with numbers with numpy functions

    a=np.zeros((5,7,3))
    # print(a)

    a = np.ones((5, 7, 3))
    # print(a)

    a=np.full((5,3,7),9)
    # print(a)

    a=np.empty((8,4,2))
    # print(a)

    #train a model and dont want to have a biased input for random starting point
    a=np.random.random((5,5,5))
    # print(a)

    #range values
    a=np.array([0,5,10,15,20,25,30])
    b = a*2-a ** 2
    # print(b)

    #range value
    a=np.arange(0,1000, 5)
    b=np.sin(a)
    # print(a)
    # print(b)

    #linspace
    a=np.linspace(0,50,100,dtype=int)
    # print(a)


    #attributes of array

    a=np.array(
        [
            [
                [2,3,4,5],
                [6,7,8,9],
                [6,3,2,1]
            ],
            [
                [6,7,8,9],
                [10,3,5,3],
                [3,4,5,6]
            ]
        ]
    ,dtype=int
    )
    # print(a.shape,a.size,a.ndim,a.dtype)
    # print(np.exp(a), np.sqrt(a),np.log(a))
    # a.sort()

    # print(a.max(),a.min())

    print(np.median(a),np.std(a))