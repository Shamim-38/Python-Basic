'''
@Author     : Md. Shamimul Islam
@Written    : 10/02/2019
@Description: python For Loop
'''
sequence=[55,3,2,None,0,10,None]
total=0
for value in sequence:
    if value is None:
        continue
    else:
        total+=value
print(total)        


seq=[1,2,3,0,8,1,7,5]
total=0
for value_5 in seq:
    if value_5==5:
        break
    else:
        total+=value_5
print(total)   

# Iterating over a list 
print("-------------List Iteration------------") 
m=['i','am','miuan']
for i in m:
    print(i)

# Iterating over a tuple
print("-----------------tuple Iteration------------------") 
n=('u','are','great')
for i in n:
    print(i)

l=['i','love','u']
for i in range(len(l)):
    print(l[i])
else:
    print("it is ok")    


print("------nested for loop------------")
for i in range(4):
    for j in range(4):
        if j>i:
            break
        print(i,j)

print("-------control flow-------------")
# It returns the control to the beginning of the loop.
# Prints all letters except 'e' and 's'
for i in "bangladesh":
    if i=="s" or i=="a":
        continue
    print("current letter",i)

#It brings control out of the loop 
# break the loop as soon it sees 'e'  
# or 's' 
print('------2----------')
for i in "bangladesh":
    if i=="s" or i=="a":
        break
    print(i)
