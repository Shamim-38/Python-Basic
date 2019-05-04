'''
@Author     : Md. Shamimul Islam
@Written    : 02/03/2019
@Description: python control flow
'''
"""
the operating system path is submodule of operating system module
"""

import os

#show just file name
file_name=os.path.basename('/home/Documets/Python/os_pyt_02.py')
print(file_name)

#show the directory file
folder_name=os.path.dirname('/home/Documents/Python/os_pyt_02.py')
print(folder_name)

#check a file or folder ,whether is it exist?
print(os.path.exists('/home/Documents/Python/os_pyt_02.py'))

#check a directory,whether is it exits?
print(os.path.isdir('/home/Documents/Python'))

#check a file,whether is it exists?
print(os.path.isfile('/home/Documents/Python/os_pyt_02.py'))

#join a file into a folder
dir=os.getcwd()
print(dir)
os.path.join(dir,'text_py.py')
print(os.path.exists('/home/Documents/Python/text_py.py'))
