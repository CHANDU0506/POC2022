# Calculate Persons age Based on year of Birth
from cmath import nanj


name = str (input("Please Enter Your good Name:"))
year= int (input("Please enter the year you are born: "))
print (year)
currentage= 2022 - year
months = currentage*12
days = currentage*365
print("Hello "+ name+".You are %d years old."%(currentage))
print("Hello "+ name+".You are %d months old."%(months))
print("Hello "+ name+".You are %d days old."%(days))
