import numpy as np

#sum
stud_marks=np.array([78,92,36,64,89,45])
print(np.sum(stud_marks))

additional_marks=np.array([2,4,3,2,1,3])
stud_marks+=additional_marks
print(stud_marks)
stud_marks=np.add(stud_marks,additional_marks)
print(stud_marks)