import calendar  
# Enter the month and year  
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
  
# display the calendar  
if mm in range(1,13):
    print(calendar.month(yy,mm))  
else :
    print("Incorrect input")