'''
@Author     : Md. Shamimul Islam
@Written    : 08/02/2019
@Description: python String Basic
'''

a='the string is short'
b="another way"
c="""the srting is short
the string is long
the string is good"""

c=c.replace('string','long string')

print(c)
print(c.count('\n'))

d='python'
print(list(d))
print(tuple(d))
print(d[:3])
#print(d(:4))
#escape special characters
x='12\\12'
print(x)
y='this\\has\\no\\special\\characters'
print(y)
z=r'this\has\no\special\characters'
print(z)

i='this is the first half'
j='and this is the second half'
e=i+j
print(e)
exit()
