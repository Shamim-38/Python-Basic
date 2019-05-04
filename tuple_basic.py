'''
@Author     : Md. Shamimul Islam
@Written    : 10/02/2019
@Description: python Tuple Basic
'''
tupl=4,3,6
print(tupl)
#nested for tuple
print("--------------nested for tuple----------")
nes_tuple=(4,3,2),(8,2)
print(nes_tuple)
#convert to a tuple
print("----------convert to a tuple-----------")
tupl_0=tuple([3,5,3])
tupl_1=tuple('welcome')
print('{}\n{}'.format(tupl_0,tupl_1))

#tuple internal append
print("-------------tuple internal append----------")
tupl_2=(None,9,[1,3,4],'a')
print(tupl_2)
tupl_2[2].append(7)
print(tupl_2)
#concatenate tuples using the + operator
print("------------concatenate--------------")
tupl=tupl+(2,)
print(tupl)
def main():
    #create a tuple
    tup=(2,8,6,0,3)
    print("************* Append in a tuple at the end ***********")
    print("Original tuple: ",tup)
    tup=tup+(15,)
    print("modified tuple: ",tup)
    print('********** modify or replace on the tuple in a specific index**************')
    n=2
    tup=tup[:n]+('add',)+tup[n+1:]
    print("modified tuple: ",tup)
    print("******************delete a specific index*******************")
    tup=tup[:n]+tup[n+2:]
    print("Delete two index: ",tup)
if __name__=='__main__':
    main()    
