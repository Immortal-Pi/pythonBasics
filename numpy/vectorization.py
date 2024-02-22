import numpy as np

#sum
stud_marks=np.array([78,92,36,64,89,45])
print(np.sum(stud_marks))

additional_marks=np.array([2,4,3,2,1,3])
stud_marks+=additional_marks
print(stud_marks)
stud_marks=np.add(stud_marks,additional_marks)
print(stud_marks)


#broadcasting
a=np.array([1,2,4])
b=np.array([[5],[3],[2]])
print(b*a)

#problem statement
stud_marks1=np.array([[67,45],[90,92],[66,72],[32,40]])
# Now the teacher wants to award extra five marks in Chemistry and extra ten marks in Physics
additional_marks1=np.array([5,10])
print(stud_marks1+additional_marks1)

