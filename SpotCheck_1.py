# William Craddock
# 13/10/2014
# Spot Check 1

attendance = int(input("Please enter your Attendance as a Percentage: "))
if attendance > 85 and attendance <= 100:
    print("Your attendance is {0}%. Keep up the good attendance.".format(attendance))
elif attendance <= 85 and attendance >= 0:
    print("Your attendance is only {0}%. You must improve your attendance.".format(attendance))
else:
    print("Please try again. Invalid result.")
