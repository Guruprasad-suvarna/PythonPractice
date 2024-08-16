import calendar

year=int(input("Enter the year.."))
for i in range(1,13):
   lastDay=calendar.monthrange(year,i)[1]
   weekday= calendar.weekday(year,i,lastDay)
   if weekday == 5:
        print(f"{i}""/"f"{lastDay-1}""/"f"{year}")
   elif weekday == 6:
         print(f"{i}""/"f"{lastDay-2}""/"f"{year}")
   else:
          print(f"{i}""/"f"{lastDay}""/"f"{year}")