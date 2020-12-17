# Find the length of the below string
#
# String_1="GreensTechnology"
# String_2="Python Programming"
# String_3="s e l e n i u m"
# String_4="9876543210"
# String_5="Hi welcome to the world of programs"
# print(len(String_1))
# print(len(String_2))
# print(len(String_3))
# print(len(String_4))
# print(len(String_5))

# Find the index position
#
# s='Programming languages are c,c++,Java and Python'
# i=s.index('c')
# print(i)
# print("Find the index of Java",s.index('Java'))
#
# print("Find the index of g ",s.index('g'))


# Using find method perform the below operations
# s= 'Selenium automation using Python'
# s1=s.find('automation')
# s2=s.find('using')
# print (s1,s2)

# Given String is "Welcome to Python class" and find the substring
# s = "Welcome to Python class"
# print(s[5])
# print(s[5:12])
# print(s[9:20])
# print(s[-5:-1])

# Find whether the string python is present or not using 'if'

# s='Programming languages are c,c++,Java and Python'
# if (s.find('c') == -1):
#     print("NO")
# else:
#     print("YES")


# Given String as "Welcome to Python class" and split it by space.
# Input = "Welcome to Python class."
# data = Input.split(" ")
# for temp in data:
#     print (temp)

# Input = "Welcome to Python class."
# data = Input.split(" ",1)
# for output in data:
#     print (output)

# Find the count of word "is"
# s="Python is awesome and it is dynamic language"
# count=s.count('is')
# count1=s.count('i')
# print("the count of 'is' in the given string : ",count)
# print("the count of 'i' in the given string : ",count1)

# Given String as "Welcome" and count the number of consonants and vowels

# string = 'Welcome'
# vowels = 0
# consonants = 0
# for i in string:
#     if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#         vowels = vowels + 1
#     else:
#         consonants += 1
#
# print("Number of vowels are:")
# print(vowels)
# print("Number of consonants are:")
# print(consonants)
#
# Get two input strings from user and Compare
#
# String_1='Java'
# String_2 ='Javi'
# print(String_1==String_2)


# Given String as "Welcome to Python class" and verify whether the given string startsWith welcome
#
# s='Welcome to Python class'
# s1='Hai I am from Greens'
# print(s.startswith('Wel'))
# print(s1.endswith('Wel'))

# Get the input from the user and print that word in lowercase/uppercase
# Input='GREENS TECH '
# print(Input.lower())

# Get the input from the user and print the first letter in capital
# s= 'selenium with PYTHON'
# print(s.capitalize())

# Remove the unwanted spaces from the given string
#
# s= "      Incredible India        "
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())