'''
@Author     : Md. Shamimul Islam
@Written    : 02/03/2019
@Description: python Operating System Basic
'''

import os

"""
getcwd()
The getcwd() method returns the current working directory in the form of a string
"""
#print(os.getcwd())

"""
chdir()
chdir() is the Python equivalent of cd. Call the method and pass it the directory that you want to change to as a string. 
"""

os.chdir('/home/shamim/Documents')
#print(os.getcwd())
#go back perents dir
os.chdir('../')
#go back Documents folder
os.chdir('/home/shamim/Documents/Python') 
print(os.getcwd())
"""
make directory
"""
os.mkdir('new_folder')
documents_list=os.listdir('/home/shamim/Documents/Python')
print(documents_list)

""""
make directories
"""
os.makedirs('1/2/3/4/5')
documents_list=os.listdir('/home/shamim/Documents/Python')
print(documents_list)

"""
remove operation
"""
#remove a file
os.remove('t.py')
#remove a directory
os.rmdir('1')

"""Rename"""
os.rename('ty.py'.'ty_1.py')

