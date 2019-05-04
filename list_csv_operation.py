'''
@Author     : Md. Shamimul Islam
@Written    : 10/02/2019
@Description: python List and CSV operation
'''
print("--------------Make a list of list from a csv file---------------")
import csv
fp=open('Advertising.csv',"Ur")
data_list=[]
for line in fp:
    data_list.append(line.strip().split(','))
    #strip = remove space in the first and end of the tuple
    #stlit=seperated by comma after every tuple's element
fp.close
print(data_list)   
for line in data_list:
    print(','.join(line))

"""
#function 
def load_file(filename):
    fp = open(filename, 'Ur')
    data_list = []
    for line in fp:
        data_list.append(line.strip().split(','))
    fp.close()
    return data_list
#advanced python
def load_file(filename):
    with open(filename, 'Ur') as fp:
        data_list = [tuple(line.strip().split(",") for line in fp]
"""
print("--------------Write a CVS file from a tuple datasets---------------")
def save_file(filename,data_list):
    fp=open(filename,'w')
    for line in data_list:
        fp.write(','.join(line) + '\n')
    fp.close    
save_file('b.csv',data_list)        

data_list=(('2','4','3'),('6','0','8'))
save_file('b_1.csv',data_list)
