def patternPyramid(number):
    for i in range(0,number*2):
        rowj=''
        if i%2==0:
            for j in range(0,i+1):
                rowj=rowj + 'H'

            print(rowj.center(number*2,' '))