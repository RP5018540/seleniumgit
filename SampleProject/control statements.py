
#emp_ID=1
#emp_name='John'
#empl_email_id='john1@gmail.com'
#emp_phone_no=9874563211
#emp_salary=20000
#emp_gender='Male'
#emp_city='chennai'
#print(emp_ID)
#print("emp_Id")

# student_Id=int(input("Enter the student ID: "))
# student_Name=str(input("Enter the student name: "))
# Mark_1=int(input("Enter the marks in tamil: "))
# Mark_2=int(input("1nter the marks in English: "))
# Mark_3=int(input("Enter the marks in Maths: "))
# Mark_4=int(input("Enter the marks in Science: "))
# Mark_5=int(input("Enter the marks in Social: "))
# Sum=(Mark_1+Mark_2+Mark_3+Mark_4+Mark_5)
# Average=(Sum/5)
# percentage=(Sum / 500) * 100
# print(Sum)
# print(Average)
# print(percentage)

#control statements
#
# for x in range(1, 100):
#     if (x == 5):
#         print(x)
# #O/P=5


# for x in range(1,100):
#     if(x==5):
#         break
# print(x)
#O/P=5

# for x in range(1,100):
#     if(x==5):
#         continue
# print(x)
# O/P=99

# for x in range(1,4):
#    for y in range(1,4):
#        print(y)
# print(x)
#
# O/P=1
# 2
# 3
# 1
# 2
# 3
# 1
# 2
# 3
# 3

# for x in range(1,4):
#    for y in range(1,4):
#        print(x)
# O/P=    1
# 1
# 1
# 2
# 2
# 2
# 3
# 3
# 3


# for x in range(1,4):
#    for y in range(1,x):
#        print(y)
# o/P=1
# 1
# 2

# for x in range(1,4):
#    for y in range(x+1,4):
#        print(y)
# O/P=   2
# 3
# 3
#
# for x in range(1,4):
#    for y in range(x+1,x):
#        print(y)
#
# no output
#
# i=5
# if i==5:
#
#     break

# Write a program to print even/Odd number from 1 to 100
#
# i=1
# for i in range(1,101,+1):
#    if (i%2==0):
#        print(i)

# i=1
# for i in range(1,101,+1):
#    if (i%2!=0):
#        print(i)
#

# program will show if the person is eligible to vote

#
# age=int(input("Age of the voter: "))
# if(age>18):
#     print("valid voter")
# else:
#     print("invalid age to vote")

# Write a program to find even or odd number
#
# Num=int(input("Enter the number: "))
# if(Num%2==0):
#     print("It is an even no")
# else:
#     print("It is an odd no")
#
#  Find the sum of odd number 1 to 100
#
# i=1
# sum=0
# for i in range(1,101,+1):
#     if (i%2!=0):
#         print(i)
#         sum += i
# print(sum)

#
# b=str(20+"10")
# print(b)
#
# for x in range(1,4):
#    for y in range(1,4):
#        print(x)

# # reverse a number
# Num = int(input("Please Enter the Number: "))
# Reverse = 0
# while (Num > 0):
#     Reminder = Num % 10
#     Reverse = (Reverse * 10) + Reminder
#     Num = Num // 10
# print(" Reverse of entered number is = ",Reverse)

#Sum of digits

# n=int(input("Enter a number:"))
# total=0
# while(n>0):
#     digit=n%10
#     total=total+digit
#     n=n//10
# print("The total sum of digits is:",total)

#Count of digits

# n=int(input("Enter a number:"))
# Count = 0
# while(n > 0):
#     n = n // 10
#     Count = Count + 1
# print("Number of Digits in a given number = ", Count)

# Sum of elements in list
#
# list1=[20,86,79,25]
# total=sum(list1)
# print(total)

# String Reverse:

# a="Python is an interpreted langauage"
# reversed=a[::-1]
# print(reversed)

#Write a program to find the factorial of a number.

# num = int(input("Enter a number: "))
# factorial = 1
# if num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)

#
# # Fibonacci Series
#
#
# a = 0
# b = 1
# # print(a)
# # print(b)
# for i in range(1,101,+1):
#   c=a+b
#   if c>100:
#     break
#   print(c)
#   a = b
#   b = c
#
#
# num1, num2 = 0, 1
# count = 0
#
# print("Fibonacci sequence:")
# while count < 10:
#     print(num1, end="  ")
#     temp = num1 + num2
#     # update values
#     num1 = num2
#     num2 = temp
#     count += 1
























