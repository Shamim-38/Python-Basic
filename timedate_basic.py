'''
@Author     : Md. Shamimul Islam
@Written    : 08/02/2019
@Description: python TimeDate
'''
from datetime import datetime, date, time
dt = datetime(2019, 1, 2,00,33,33)
#dt = datetime(2029,1,1)
print(dt.month)
print(dt.minute)
#dt=dt.strftime('%d-%m-%y %H:%M:%S')
print(dt)
dt1=datetime(year=2000,month=2,day=8,hour=8,minute=34)
print(dt1)
dt1=dt1.replace(year=2001,month=4,day=5,hour=3,minute=0)
print(dt1)
dt2=dt-dt1
print(dt2)
#current time
now= datetime.now()
today=now.date()
print(today)
moment=now.time()
print(moment)
now=datetime.combine(today,moment)
print(now)
