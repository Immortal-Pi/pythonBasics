import matplotlib.pyplot as plt
import pandas as pd


# nationality=['american','german','french','asian']
# students=[60,20,21,70]
#
# #extract
# explode=[0.2,0,0,0]
#
# # plt.pie(students,labels=nationality,autopct='%.2f%%',shadow=True,explode=explode)
#
# pairs = zip(nationality,students)
# pairs= sorted(list(pairs))
# nationality, students = zip(*pairs)
#
# plt.pie(students, labels=nationality, autopct='%.2f%%',shadow=True,explode=explode,counterclock=False,startangle=90)
# plt.title('Student Nationality')
#
# plt.show()

# schools=['NMIT','MSRIT','SVCE','SVIT']
# avg_marks=[97,98,60,55]
# explode=[0.3,0,0,0]
# # plt.pie(avg_marks,labels=schools,autopct='%.2f%%',shadow=True,startangle=30,explode=explode)
# pairs=zip(schools,avg_marks)
# pairs=sorted(pairs)
# schools,avg_marks=zip(*pairs)
# plt.pie(avg_marks,labels=schools,autopct='%.2f%%',shadow=True,startangle=30,explode=explode)
# plt.show()


data=pd.read_csv('datasets/auto-mpg.csv')

condition=data['horsepower']=='?'
data['horsepower']=data['horsepower'].mask(condition,None)
data.dropna(inplace=True)

print(data.columns)
data2=data.groupby('origin').count()[['car name']]
data2.reset_index(inplace=True)
plt.pie(data2['car name'],labels=data2['origin'])
plt.show()


