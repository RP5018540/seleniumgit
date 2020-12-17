# # Perform Operator Overloading Using +
#
# class Add:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self, other):
#         self.other=other
#         return self.a+other.a
# A1=Add(10)
# A2=Add(20)
# A3=Add("Greens")
# A4=Add("Tech")
# sum1=A1+A2
# sum2=A3+A4
# print(sum1)
# print(sum2)


# Perform Operator Overloading Using *


# class Multi:
#     def __init__(self,a):
#         self.a=a
#     def __mul__(self, other):
#         self.other=other
#         return self.a*other.a
# A1=Multi(3)
# A2=Multi("Greens")
# A3=Multi("Tech")
#
# mul1=A1*A2
# mul2=A1*A3
# print(mul1)
# print(mul2)


# Perform Operator Overloading Using len() method

# class Length:
#     def __init__(self,a):
#         self.a=a
#     def __len__(self):
#         return len(self.a)
# a="Greens"
# b=[10,20,30,40]
# c=20,67,99,89,30
# d={90,40,50,60,70}
#
# print(len(a))
# print(len(b))
# print(len(c))
# print(len(d))

# overload the method emp_Id() based on different Number of arguments;

# class Employee():
#     def emp_details(self,name=None,EmpID=None):
#         print(name,EmpID)
# Obj=Employee()
# Obj.emp_details('Radhika',123)
# Obj.emp_details('Ritu',258)



# override the method deposit in BankInfo

# class Bankinfo():
#     def saving(self):
#         print('For saving account interest is 5%')
#     def deposit(self):
#         print('For deposit no extra charge')
# class AxisBank(Bankinfo):
#     def deposit(self):
#         print('For deposit extra charges are applied')
# B=AxisBank()
# B.deposit()
# B.saving()

# class Bike():
#     def speed(self):
#         print('speed of the bike differs based on models')
#     def cost(self):
#         print ('the cost of the bike differs based on models')
# class ktm():
#     def speed(self):
#         print('speed of the bike ktm is 120')
#     def cost(self):
#         print ('the cost of the bike ktm is 2L')
# O=ktm()
# O.cost()
# O.speed()

