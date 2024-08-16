from datetime import date
from dateutil import *
#import datetime

#now=datetime.datetime.now()
#print(now)
from dateutil.relativedelta import relativedelta,  MO
 


todayDate=date.today()
print(todayDate)


lastMonday=todayDate+relativedelta(weekday=MO(-1))
print(lastMonday)
