#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ADMIN
#
# Created:     13-08-2022
# Copyright:   (c) ADMIN 2022
# Licence:     <your licence>
#------------------------------------------------------------
n=int(input("Enter the desired number "))
p=n
num=0
while(n!=0):
    r=n%10
    n=n//10
    num=(num*10+r)
if(num==p):
    print("the required number is palindrome ")
else:
    print("The number is not palindrome ")
