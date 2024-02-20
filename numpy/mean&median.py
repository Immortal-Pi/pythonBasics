import numpy as np



students_mark=np.array([10,20,40,50,33],dtype=float)
students_names=np.array(['amruth','akshath','sharath','subhodh','chiranth'],dtype=str)
stud=np.array([students_mark,['amruth','akshath','sharath','subhodh','chiranth']])

#mean, meadian, min and max
# print(f'mean: {np.mean(students_mark)}')
# print(f'median: {np.median(students_mark)}')
# print(f'min: {np.min(students_mark)}')
# print(f'max: {np.max(students_mark)}')
#
# #argmax and argmin returns the index of min and max vales
# print(f'argmin: {np.argmin(students_mark)}')
# print(f'argmax: {np.argmax(students_mark)}')
#
# #where function
# x=np.where(students_mark>20)
# print(x,students_mark[x])

#filtering
# print(students_mark)
# array2=students_mark>20
# print(array2,students_mark[array2])


#sorting 2 methods 
# array2=np.sort(students_mark)
students_mark.sort()
print(students_mark)