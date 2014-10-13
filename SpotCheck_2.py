# William Craddock
# 13/10/2014
# Spot Check - 2

first_name = input("Please enter your First Name: ")
last_name = input("Please enter your Last Name: ")
gender = input("Please enter your your Gender (male/female): ")
print()
if gender == "male":
    print("Mr {0} {1}.".format(first_name,last_name))
elif gender == "female":
    print("Ms {0} {1}.".format(first_name,last_name))
else:
    print("Please enter an appropriate gender")
