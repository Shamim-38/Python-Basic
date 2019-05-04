'''
@Author     : Md. Shamimul Islam
@Written    : 04/02/2019
@Description: python Variable Argument Passing
'''

a=[1,2,3]
b=a
a.append(4)
print(b)  #some others languages(c,java) don't dynamic assign like python

c=5
print(type(c))
d='s'
print(type(d))
print(isinstance(c,int))
