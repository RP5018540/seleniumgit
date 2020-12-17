# Create the above functions without arguments
# def emp_Id():
#     print ("EMP ID is 123")
# def emp_Name():
#     print("EMP Name is Ritu")
# def emp_phone():
#     print("EMP phone no is 987456321")
# def emp_Dob():
#     print("EMP dob is 1/2/89")
# emp_Dob()
# emp_phone()

# Create the above functions with passing some arguments

# name='Green_Technologies'
#
# def greens_Omr(name,address):
#     print(name, "address is",address)
# def greens_Tambaram(name,address):
#     print(name, "address is",address)
# def greens_Velacherry(name,address):
#     print(name, "address is",address)
# def Anna_Nagar(name,address):
#     print(name, "address is",address)
#
# greens_Omr(globals()['name'],'7,gandhi st,OMR')
# greens_Tambaram('Green_Technologies','122,gandhi stTambaram')

# Sum and sub function:

# def Addition(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# def subtraction(c,d):
#     sub=c-d
#     print(sub)
#     return sub
# Addition(10,86)
# subtraction(78,89)
# Addition(98,186)
# subtraction(128,89)

# returntype of multiple values
#
# def calculator(*str):
#     for s in str:
#         print(s)
#
# calculator(1,589,789,258,'Add','Sub')



# Find the output for the below function


# def my_function(fname, lname):
#     print(fname + " " + lname)
#
#
# my_function("Harry")
#
# O/P-Missing argument

# def my_function(country = "Norway"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
# o/p
# I am from Sweden
# I am from India
# I am from Norway
# I am from Brazil


# Create the below functions with three arguments with the default return type
# def company_details(comp_name='Atos'):
#     print('Company name is', comp_name)
# def employee_details(EMPID=123,EMP_name='Ritu'):
#     print(EMPID,'of employee name is ',EMP_name)
# company_details()
# company_details('cts')
# employee_details()
# employee_details(125,'kavi')

# Find output:

# def computer_names(*names):
#   print(names)
# computer_names(name1="hp",name2="sony",name3="dell")
#
# No Output:
# TypeError: computer_names() got an unexpected keyword argument 'name1'


# Create a function named as country_details and pass the above arguments ,print the values one by one
# def country_details( country_name,area_covered,country_population,no_of_states,no_of_unionterritories):
#     print("The country name is", country_name)
#     print("The area covered are " , area_covered)
#     print("The population is" , country_population)
#     print("states count" ,no_of_states)
#     print("unionterritories count is" , no_of_unionterritories)
# country_details('india',46,'13C',36,4)

# program for factorial of 5 using recursion

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# i=factorial(5)
# print(i)



# Create a recursive function to print "Welcome" 100 times
#
# count=0
# def recursion():
#     global count
#     print("welcome", count)
#     count+=1
#     if count==100:
#         return
#     recursion()
# recursion()


# Create a recursive function of your own and print the word "Pyhon"

# def recursive_function():
#     print("python")
#
# recursive_function()

# Using lambda function perform addition,subtraction and multiplication
#
# x=lambda a,b,c:a+b+c
# print(x(1,2,10))
# y=lambda a,b:a-b
# print(y(10,58))
# Z=lambda a,b:a*b
# print(Z(10,58))

# Using lambda function perform cube of given number
# x=lambda a:a*a*a
# print(x(2))

# Using lambda function perform squareroot of given number
# x=lambda a:a*a
# print(x(2))
#
# Input=[2, 4, 8, 11, 24, 10, 3, 27]
# result=[]
# x=lambda a:a%2==0
# result=list(filter(x,Input))
# print(result)

# Using map write a program to double each item in a list
#
# Input=[2, 4, 8, 11, 24, 10, 3, 27]
# result=[]
# x=lambda a:a*a
# result=list(map(x,Input))
# print(result)

# Using reduce write a program to add the numbers

# import functools
# from functools import reduce
# list = [1,2,3,4]
# sum =reduce(lambda x,y: x + y,list)
# print(sum)

# Using reduce write a program to multiply the numbers

# from functools import reduce
# list = [2,6,11,24,27]
# product =reduce(lambda x,y: x * y,list)
# print(product)