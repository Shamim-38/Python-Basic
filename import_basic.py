'''
@Author     : Md. Shamimul Islam
@Written    : 08/02/2019
@Description: python Import from module 
'''
import some_module 

result=some_module.f(4)
pi=some_module.Pi

print(result)
print(pi)

#equivalently 
from some_module import f,g,Pi
result01=g(result,pi) 
print(result01)

#equivalently
import some_module as sm 
from some_module import Pi as p,g as gf
result02=sm.f(9)
result03=sm.gf(2,p)

print(result02)
print(result03)
