'''
@Author     : Md. Shamimul Islam
@Written    : 06/02/2019
@Description: python Convert data type
'''

val = "español"
print(type(val))
val_update=val.encode('utf-8')
print(val_update)
val=val_update.decode('uft-8')
