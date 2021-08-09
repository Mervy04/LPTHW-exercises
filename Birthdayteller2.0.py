#import datetime module


#from datetime import date
import datetime

x = datetime.datetime.now()

y = x.year
m = x. month
d = x.day

xx = x.year, x.month, x.day

print(x)
py
#create input message for user to input his birth date

year = int(input("What year were you born? "))
month = int(input("What month were you born? "))
day = int(input("What day were you born? "))

#we use if else conditions to differentiate the dates.

if day > d and month >= m: #if the day of birth is > than todays date and your month of birth is >= than todays month.
    dd = (d + 30) - day #todays date + 30 (days/ a month) - your birth day would be assigned to a new variable dd
    mm = ((m -1) + 12) - month #variable mm = present month - 1(month) + 12 - your month of  birth
    yy = (y -1) - year #variable yy = present year -1- year of birth
py
    print(str(yy) + " Years" + str(mm) + " Months" + str(dd) + " Days")

#we copy and paste the above but use elif statement

elif day > d and month < m: #this is if the above doesnt work. else if day of birth > todays day and month of birth < todays month
    dd = (d + 30) - day #variable dd = todays day + 30 - day of birth
    mm = m - month #variable mm = todays month -month of birth
    yy = y - year #variable yy = present year - year of birth

    print(str(yy) + " Years" + str(mm) + " Months" + str(dd) + " Days")

elif day < d and month > m:
   dd = d - day
   mm = (m  + 12) - month
   yy = (y -1) - year


   print(str(yy) + " Years" + str(mm) + " Months" + str(dd) + " Days")

else:
     dd = d - day
     mm = m- month
     yy = y - year


     print(str(yy) + "Years" + str(mm) + "Months" + str(dd) + "Days")

days_till_next_bd = datetime.datetime(y + 1, month, day) - x
days_till_next_bd_this_year = datetime.datetime(y,month, day) - x
print("%s days until your next birthday." % days_till_next_bd.days)
print("%s days till your birthday this year." % days_till_next_bd_this_year.days)


