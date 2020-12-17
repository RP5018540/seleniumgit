#
# Create a File  in "D:\\File Operations\\read.txt with "r" mode and close file
#              a.Check whether file is readable or not?
#              b.Check whether file is writable or not?
#              c.Check whether file is closed or not?
# f=open('D:\\file operations.txt','w')
# f.write("something")
# f.close()

# :Create a File with "a" mode and close file
#              a.Check whether file is readable or not?
#              b.Check whether file is writable or not?
#              c.Check whether file is closed or not?
#
# f=open('Project1.py','a')
# f.write('green technologies')
# f.close()

#
# Create a File  in "E:\\File\\append.txt with "x" mode and close file
#              a.Check whether file is readable or not?
#              b.Check whether file is writable or not?
#              c.Check whether file is closed or not?
#
# f=open('abc.py','x')
# f.write('green technologies')
# f.close()
#
# Create a File  in "E:\\Python Notes\\read.txt with "w" mode and follow below steps
#              Step 1: Write the below content in line by line
#                      Java Class
#                      Python Class
#                      Selenium Class
#                      Mobile Testing Class

# f=open('abc.py','r+')
# f.write('Java Class')
# f.write('Python class')
# f.write('C++ Class')
#
# with open('abc.py','a',newline='') as f:
#    f.write("[100,vel,vel@gmail.com]\n")
#    f.write("[200,Nisha,Nisha@gmail.com]\n")
#    f.write("[300,Bala,Bala@gmail.com]\n")
#    f.write("[400,Ganesh,Ganesh@gmail.com]\n")
#
#
# with open('abc.py','r',newline='') as f:
#     i=f.read(100,)
#     print(i)

# # Image copying:
#
# f=open('D:\\venkat.JPEG','rb')
# f1=open('E:\\venkat_photo.JPEG','wb')
# for i in f:
#     f1.write(i)


# :Create a CSV File for 10 Employee Details
# import csv
# with open('student.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(["SN", "Name", "Department"])
#     writer.writerow([1, "Ram", "ECE"])
#     writer.writerow([2, "Tim", "CSC"])
#     writer.writerow([3, "Kavi", "EEE"])
#     writer.writerow([4, "Ramu", "ECE"])
#     writer.writerow([5, "Timy", "CSC"])
#     writer.writerow([6, "Kavitha", "EEE"])
#     writer.writerow([7, "Ramya", "ECE"])
#     writer.writerow([8, "Timothi", "CSC"])
#     writer.writerow([9, "Kaviya", "EEE"])
#
# import csv
# with open('student.csv', 'r', newline='') as f:
#     r = csv.reader(f)
#     for row in r:
#         print(row)

# Working with Zip file:

# f=open('day1task.txt','w+')
# f.write('introduction of python')
# f.close()
#
# f=open('day2task.txt','w+')
# f.write('basics of python')
# f.close()
#
# import zipfile
# task=zipfile.ZipFile('Taskinfo.zip','w')
# task.write('day1task.txt',compress_type=zipfile.ZIP_DEFLATED)
# task.write('day2task.txt',compress_type=zipfile.ZIP_DEFLATED)
# task.close()

# import zipfile
# Extract=zipfile.ZipFile('Taskinfo.zip','r')
# Extract.extractall('taskdetails')

#
# Description :Create a folder JavaNotes in Local Disk D using Os Module
#              a.Check whether it is directory or not
#              b.Check whether it is file or not


# import os
# # os.mkdir("d:\\Javanotes")
# # print (os.listdir("d:\\Javanotes"))
# # os.getcwd()
# os.remove("d:\\Javanotes")

# import os
# print(os.listdir("D:\\"))

# import  os
# print(os.walk("D:\\Downloads"))