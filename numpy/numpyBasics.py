import numpy as np
import time




#list vs numpy array

# list1=list(range(1,100000))
# list2=list(range(2,100001))
#
# list3=[]
# start_time_list=time.time()
# for i in range(len(list1)):
#     list3.append(list1[i]+list2[i])
# end_time_list=time.time()
#
# start_time_np=time.time()
# numpy_array1=np.arange(1,100000)
# numpy_array2=np.arange(2,100001)
# numpy_array3=numpy_array1+numpy_array2
# end_time_np=time.time()
#
# print(f'Time\n list operation :{end_time_list-start_time_list}\n numpy operation :{end_time_np-start_time_np}')

students_mark=np.array([10,20,40,50,33],dtype=float)
students_names=np.array(['amruth','akshath','sharath','subhodh','chiranth'],dtype=str)
stud=np.array([[10,20,40,50,33],['amruth','akshath','sharath','subhodh','chiranth']])
print(stud,stud.shape,students_mark.dtype)


#changing datatypes
# stud_array=np.array(students_mark,dtype=int)
# print(stud_array.dtype)


# #accessing elements from 1D array
# print(students_names[0])
#
# #accessing elements from 2d array
# print(stud[1])
# #accessing the elements in the second row i.e. 1 represents the second row and 0 represents the first element
# print(stud[1,0])
# #negitive number for elements from back
# print(stud[1,-1])

#slicing 1D array
cars = np.array(['chevrolet chevelle malibu', 'buick skylark 320', 'plymouth satellite', 'amc rebel sst', 'ford torino'])
print(cars[1:4])

#slicing 2D array
print(stud[0:2]) #gives first 2 rows

print(stud[0:2,1:3]) #from first 2 rows give values at index 1 to 3



