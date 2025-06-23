#  سال کبسه
while True:
    def is_leap(year):
       if year % 400 == 0 or(year % 100 != 0 and year % 4 == 0):
           return True
       else:
           return False
    year = int(input(' Enter a year: ').strip())
    if year==0:
        break
    print(is_leap(year))
print("end")