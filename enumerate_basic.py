'''
@Author     : Md. Shamimul Islam
@Written    : 12/02/2019
@Description: python enumerate basic
'''
a_list=['one','two','three']
mapping={}
for i,value in enumerate(a_list):
    mapping[value]=i
print(mapping)    
