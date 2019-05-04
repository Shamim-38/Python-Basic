'''
@Author     : Md. Shamimul Islam
@Written    : 11/02/2019
@Description: python List basic
'''

a_list=['2','9','3','7']
tupl=('i','a','h','9')
b_list=list(tupl)
print(b_list)
gen=range(10)
print(gen)
b_list=list(gen)
print(b_list)
print("************several operation in list****************")
print("***************append into list*******************")
print(b_list)
b_list.append("ok")
print(b_list)
print('Ok add in list:{0}'.format(b_list))
print("***************insert into list*******************")
b_list.insert(1,'one')
print('one insert into 1st index in list:{0}'.format(b_list))
print("***************pop from list*******************")
#The inverse operation to insert is pop , which removes and returns an element at a
#particular index
b_list.pop(2)
print('one pop out from 2nd index in list:{0}'.format(b_list))
print("***************remove an element from list*******************")
b_list.remove(5)
print('one remove(5) from the list:{0}'.format(b_list))
print("*****Check if a list contains a value using the -in- keyword******** ")
print("check a the element in the list:{0}".format(2 in b_list))
print("check a the element in the list:{0}".format(2 not in b_list))
print("*****Concatenating/combile  list ******** ")
c_list=a_list+b_list
print('Combine the list:{0}'.format(c_list))
print("*********Extend list ************** ")
c_list.extend(['lol','lol'])
print('Extend the list:{0}'.format(c_list))



