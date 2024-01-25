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
    print(a)