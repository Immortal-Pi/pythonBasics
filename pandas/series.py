import pandas as pd

series= pd.Series([1,2,5,3,2])
# print(series)

# print(series.values, series.index)

#accessing data in series
# print(series[1])

#slicing the data
# print(series[2:3])

series2=pd.Series(data=[5,10,1,3,4,7,3],index=['amruth','akshath','chiranth','sharath','subu','nigal','abhi'])

# print(series2)
# print(series2['akshath'])
# print(series2['akshath':'nigal'])

#dictionary to Series

dict1={
    'amruth':21,
    'akshath':22,
    'sharath':33,
    'subu':23
}
data2=pd.Series(dict1)
# print(data2)
ids={
    23:'amruth',
    24:'akshath',
    25:'sharath'
}

math_marks={
    23:50,
    24:70,
    25:90
}

data=pd.DataFrame({'student':ids,'marks':math_marks})
print(data['marks'])

