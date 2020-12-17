# Given a string, display only those characters which are present at an even index number.
#
# def printEveIndexChar(str):
#   for i in range(0, len(str), 2):
#     print("index[",i,"]", str[i] )
#
# inputStr = "pynative"
# print("Orginal String is ", inputStr)
#
# print("Printing only even index chars")
# printEveIndexChar(inputStr)
#
# Removing characters from a string starting from zero up to n and return a new string
#
# def removeChars(str, n):
#   return str[n:]
#
# print("Removing n number of chars")
# print(removeChars("pynative", 4))

# Given a list of numbers, return True if first and last number of a list is same
# def isFirst_And_Last_Same(numberList):
#     print("Given list is ", numberList)
#     firstElement = numberList[0]
#     lastElement = numberList[-1]
#     if (firstElement == lastElement):
#         return True
#     else:
#         return False
#
# numList = [10, 20, 30, 40, 10]
# print("result is", isFirst_And_Last_Same(numList))

# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

# Given list is
#
# def divisibleby5(List):
#
#     print("Given list is ", List)
#     for n in List:
#         if  n%5==0:
#             print( n)
# divisibleby5([10, 20, 33, 46, 55])


# Return the total count of sub-string “Emma” appears in the given string

# s= 'Emma is good developer,Emma is a writer'
# print('The count of “Emma” appears in the given string',s.count('Emma') )

# Reverse a given number and return true if it is the same as the original number

# def returnno(num):
#     print("The given no is ", num)
#     orinum=num
#     reverse=0
#     while(num>0):
#         remainder=num%10
#         reverse=(reverse*10)+remainder
#         num=num//10
#     if(reverse==orinum):
#         return True
#     else:
#         return False
#
# print("The original and reverse number is the same:", returnno(221))

# Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list


# List1=[10, 20, 23, 11, 17]
# List2=[13, 43, 24, 36, 12]
# res=[]
# for n in List1:
#     if n % 2 != 0:
#         res.append(n)
# for n in List2:
#     if n%2==0:
#         res.append(n)
#
# print('The result is',res )

# Write a code to extract each digit from an integer, in the reverse order
# number = 75036
# print("Given number", number)
# while (number > 0):
#     # get the last digit
#     digit = number % 10
#
#     # remove the last digit and repeat the loop
#     number = number // 10
#     print(digit, end=" ")
#
# Calculate income tax for the given income by adhering to the below rules
# Taxable Income	Rate (%)
# First $10,000	0
# Next $10,000	10
# The remaining	20
#
# income = 45000
# taxPayable = 0
# print("Given income", income)
#
# if income <= 10000:
#     taxPayable = 0
# elif income <= 20000:
#     taxPayable = (income - 10000) * 10 / 100
# else:
#     # first 10,000
#     taxPayable = 0
#
#     # next 10,000
#     taxPayable = 10000 * 10 / 100
#
#     # remaining
#     taxPayable += (income - 20000) * 20 / 100
#
# print("Total tax to pay is", taxPayable)

# Print multiplication table form 1 to 10

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end=" ")
#     print("\t\t")

# num=10
# for i in range(1, 11):
#     print(i,'x',num,'=',i * num)
# print("\t\t")


# for i in range(0, 6, 1):
#     for j in range(0, i ,-1):
#         print("*", end=' ')
#     print(" ")


# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, "Scott")
# print(sampleList)

# p, q, r = 10, 20 ,30
# print(p, q, r)

# var= "James Bond"
# print(var[2::-1])

# var1 = 1
# var2 = 2
# var3 = "3"
#
# print(var1 + var2 + var3)

# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)
#
# # calculate(5, 6)
#
# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)
#
# valueOne = 5 ** 2
# valueTwo = 5 ** 3
#
# print(valueOne)
# print(valueTwo)

# print('%d %d %.2f' % (11, '22', 11.22))

#
# f = open("List.py", "r")
# print(f.readline(3))
# f.close()

# print('[%c]' % 65)


# aTuple = "Yellow", 20, "Red"
# a, b, c = aTuple
# print(a)
#
# # n=int(input("No of rows: "))
# for i in range(5):
#     for j in range (1,i+1):
#         print(j,end="")
#     print()
#
# print(a)
# a=10

# str = "pynative"
# for i in range (0,len(str),2):
#     print(i,"**",str[i] )



# string='emma is emma'
# char='emma'
# s=len(char)
# count = 0
# for i in range(len(string)):
#     if(string[i:i+s]==char):
#         count = count + 1
#
# print(count)


# for num in range(5):
#     for i in range(num):
#         print (num, end=" ") #print number
#     # new line after each row to display pattern correctly
#     print("\n")

# num=int(input("enter the no: "))
# originalnum=num
# reversenum=0
# while(num>0):
#     remainder=num%10
#     reversenum=(reversenum*10)+remainder
#     num=num//10
# print(reversenum)
# if(originalnum==reversenum):
#     print("True")
# else:
#     print("False")

# def sumNum(num):
#     previousNum = 0
#     for i in range(num):
#         sum = previousNum + i
#         print("Current Number", i, "Previous Number ", previousNum," Sum: ", sum)
#         previousNum = i
#
# print("Printing current and previous number sum in a given range(10)")
# sumNum(10)
# print('My', 'Name', 'Is', 'James', sep='**')
# print(oct (8))
# print('%.2f'%458.541315)
# str1, str2, str3 = input("Enter three string").split()
# print(str1, str2, str3)
#
# quantity = 3
# totalMoney = 1000
# price = 450
# statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
# print(statement1.format(quantity, totalMoney, price))

# print("First 10 natural no's are: ")
# i=0
# while(i<=10):
#     print(i)
#     i+=1

# for i in range(6):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()

# sum1 = 0
# n = int(input("Please enter number "))
# for i in range(1, n + 1, 1):
#     sum1 += i
# print("\n")
# print("Sum is: ", sum1)

# n=2
#
# for j in range(1,11,+1):
#     print(n*j)

# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# for item in list1:
#     if (item > 150):
#         break
#     if(item % 5 == 0):
#         print(item)


# n=int(input("enter the no: "))
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(count)

# n=int(input("enter the no: "))
# count=0
# for i in  n:
#     i=i//10
#     count+=1
# print(count)

# for num in range(25, 50 + 1):
#
#     # if num > 1:
#         for i in range(2, num):
#
#             if (num % i) == 0:
#
#                 break
#         else:
#             print(num)

# Check the given number is odd or not
# ➢ Check the given number is even or not
# ➢ Print first 100 odd numbers
# ➢ Print first 100 even numbers
# ➢ Count the number of even numbers from 1 to 100
# ➢ Count the number of odd numbers from 1 to 100
# ➢ Find the factorial of a given number
# ➢ Generating fibbonacci series
# ➢ Find the reverse of the given number
# ➢ Check the given number is palindrome or not
# ➢ Check the given number is armstrong or not
# ➢ Find the sum of the digits in a number
# ➢ Find the number of digits in a number
# ➢ Find the product of digits in a number
# ➢ Find the reverse of the string
# ➢ Check the given string is palindrome or not
# ➢ Print each word's first letter of the given string in capital number
# ➢ Check two strings are equal
# ➢ Check two strings are Anagram or not


print(295*70)


