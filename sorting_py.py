'''
@Author     : Md. Shamimul Islam
@Written    : 12/02/2019
@Description: python Sorting
'''
a=[8,9,3,2,5,4,1,6,7]
print('sorting the list:{0}'.format(a))
b=['all','izz','ok']
b.sort(key=len)
print('Sorting by word length:{0}'.format(b))
import bisect
"""
The built-in bisect module implements binary search and insertion into a sorted list.
bisect.bisect finds the location where an element should be inserted to keep it sor‐
ted, while bisect.insort actually inserts the element into that location
#it do only correctly work in sorted list
"""
c=[1,2,2,2,3,4,5,6,7]
print(bisect.bisect(c,8))
bisect.insort(c,3)
print(c)
print('Original list is:{} \nSorted list is:{}'.format([8,94,3,2,6,7,1],sorted([8,94,3,2,6,7,1])))
print('Original list is:{} \nSorted list is:{}'.format('bangladesh agiyejao'),sorted['bangladesh agiyejao'))
