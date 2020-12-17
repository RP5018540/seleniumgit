# #hybrid inheritence
# class School:
#     def School_name(self):
#         print("The name of the school is SVM.")
#
# class Student1(School):
#     def Student1_name(self):
#         print("The name of the student1 is laksha. ")
#
# class Student2(School):
#     def Student2_name(self):
#         print("The name of the student1 is Kavi. ")
#
# class Student3(Student1, Student2):
#     def Student3_name(self):
#         print("The name of the student3 is Minu")
#
# s=Student3()
# s.Student1_name()
# s.Student2_name()
# s.Student3_name()
#
# # multilevel inheritance.
# # class Languageclass:
# #     def all_language(self):
# #         print ("All languages taken here.")
# #
# # class Tamil(Languageclass):
# #     def Tamil_langauage(self):
# #         print("tamil languages taken here.")
# #
# # class English(Tamil):
# #     def English_langauage(self):
# #         print("English languages taken here.")
# # #
# # l=English()
# # l.Tamil_langauage()
# # l.English_langauage()
#
# # Hierarchical Inheritance
# # class India():
# #     def India_States(self):
# #         print ("States present in india and theirs language.")
# #
# # class Tamilnadu(India):
# #     def TamilNadu_State(self):
# #         print("TamilNadu people speaks tamil.")
# # s1=Tamilnadu()
# # s1.India_States()
# # s1.TamilNadu_State()
# # class Kerala(India):
# #     def Kerala_State(self):
# #         print("Kerala people speaks malayalam.")
# # s2=Kerala()
# # s2.Kerala_State()
# # class AndhraPradesh(India):
# #     def AndhraPradesh_State(self):
# #         print("AndhraPradesh people speaks telugu.")
# # s=AndhraPradesh()
# # s.India_States()
#
#
#
# #
# # # Multiple inheritance
# # class College():
# #     def college_Name(self):
# #         print ("college name is WCC")
# #     def college_Code(self):
# #         print("college code is 123")
# #
# # class Dept():
# #     def dept_Name(self):
# #         print("Dep name is Physics")
# # class Student(College,Dept):
# #     def student_Name(self):
# #         print("student name is Radhika")
# #     def student_Dept(self):
# #         print("student dept is physics")
# #     def student_Id(self):
# #         print("student id is 478")
# # s=Student()
# # s.college_Code()
# # s.college_Name()
# # s.dept_Name()
#
# # Single inheritance
#
# # class LanguageInfo():
# #     def tamil_Language(self):
# #         print("tamil Language speaks in TN ")
# #     def english_Language(self):
# #         print("English Language speaks in England ")
# #     def hindi_Language(self):
# #         print("hindi Language speaks in North india ")
# # class StateDetails(LanguageInfo):
# #     def south_India(self):
# #         print("south_India people tamil,telugu and malayalam")
# #     def north_India(self):
# #         print("North_India people Hindi")
# # s=StateDetails()
# # s.hindi_Language()
# # s.south_India()
# # s.south_India()
#
# # Hierachial inheritance:
# # class Vehicle():
# #     def vehicle_Necessery(self):
# #         print("all Vehicle types")
# #
# # class TwoWheller(Vehicle):
# #     def bike(self):
# #         print("bike is two wheeler")
# #     def cycle(self):
# #         print("cycle is two wheeler")
# # class ThreeWheeler(Vehicle):
# #     def Auto(self):
# #         print("Auto is 3 wheeler")
# #
# # class FourWheeler(Vehicle):
# #     def bus(self):
# #         print('bus is 4 wheeler')
# # T=TwoWheller()
# # T.cycle()
# # T.bike()
# # T.vehicle_Necessery()
# # T1=ThreeWheeler()
# # T1.Auto()
# # T1.vehicle_Necessery()
# # T3=FourWheeler()
# # T3.bus()
# # T3.vehicle_Necessery()
#
#
#
#
#
#
#
#
#
#
#
#
b = [11,13,15,17,19,21]

print(b[::2])
