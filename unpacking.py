'''
@Author     : Md. Shamimul Islam
@Written    : 10/02/2019
@Description: python Unpacking
'''
tupl=(4,7,8,3)
a,b,c,d=tupl
print(c)
seq=[(1,2,3),(2,3,4),(5,6,7)]
for a,b,c in seq:
    print('a={0},b={1},c={2}'.format(a,b,c))
