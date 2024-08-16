import calendar

year = int(input())
d = {
0:"Monday",1:"Tuesday",2:"wed",3:"thu",4:"fri"
}
for i in range(1,13):
  lastDays=calendar.monthrange(year,i)[1]
  weekday= calendar.weekday(year,i,lastDays)
  if weekday == 5:
    print(lastDays-1," ",d[weekday-1])
  elif weekday == 6:
     print(lastDays-2," ",d[weekday-2])
  else:
      print(lastDays," ",d[weekday])