# Author: Kyle Mahoney
# Date: 9/6/2018
# ITM313 Project 1 - Payroll Program

# declare variables
payRate = 31.75

fName = ""
lName = ""

hoursWorked = 0

weeklyPay = 0
biweeklyPay = 0
monthlyPay = 0
yearlyPay = 0

# welcome user and get user input 
print ("###########################################################")
print ("Welcome to the payroll system.")
fName = input("Please enter your first name: ")
lName = input("Please enter your last name: ")
hoursWorked = float(input("Please enter the number of hours you worked this week: "))

# calculate weekly, biweekly, monthly, and yearly pay. I'm also making strings so I can concatenate easily later. 
weeklyPay = float(round(payRate * hoursWorked, 2))
stringWeekly = str(weeklyPay)

biweeklyPay = float(round(weeklyPay * 2, 2))
stringBiweekly = str(biweeklyPay)

yearlyPay = float(round(weeklyPay * 52, 2))
stringYearly = str(yearlyPay)

monthlyPay = float(round(yearlyPay / 12, 2))
stringMonthly = str(monthlyPay)

# output results
print ("###########################################################")
print ("Thank you, " + fName + " " + lName + ".\n")
print ("Your gross pay is below: \n")
print ("Weekly: $" + stringWeekly + "\n")
print ("Biweekly: $" + stringBiweekly + "\n")
print ("Monthly: $" + stringMonthly + "\n")
print ("Yearly: $" + stringYearly + "\n")
print ("###########################################################")

