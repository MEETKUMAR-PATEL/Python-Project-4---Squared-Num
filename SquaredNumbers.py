# Your code for the Task goes here
# Name:                 SquaredNumbers.py
# Author:               Meetkumar Patel
# Date Created:         Februarey 20, 2022
# Date Last Modified:   Februaury 21, 2022

# Purpose:
#
#In this program we were to use the function which generates numbersd 

#This is an empty dictinary
num = dict()
#This part of the code is a loop where x is a local variable that will
#Keep storing the value in num dictionary then the range part will be start from 1 to 10 iteratin by adding 1 in each.
ranges = range(0, 11, 0+1)
for numbers in ranges:
    #Here x is being stored in num dict then the squares are stored by values
    num[numbers] = numbers * numbers

print(num)