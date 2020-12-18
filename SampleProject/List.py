# Create a new list with values and find the length of it


# List1=[10,20,30,90,10,10,40,50]
# i=len(List1)
# print(i)
#
# List2 = [105,205,305,405,505,605,705,805]
# i=len(List2)
# print(i)
#
# List3 = ['Java','Python','Selenium','java',10,20,10]
# i=len(List3)
# print(i)

# Get the  index value

# a = [10,20,30,90,10,50]
# index=a.index(10)
# print("The index value of 10 is:" ,index)

# Append
#
# a = [10,20,30,90,10,10,40,50]
# b=[100,200,300]
# a.append(b)
# print(a)
# print("The index value of 200 is:", a[8])

# a = [10,20,30,90,10,10,40,50]
# b=[100,200,300]
# a.extend(b)
# print(a)
# index=a.index(200)
# print("The index value of 200 is:" ,index)

# Remove the value present at 2nd index and print the removed value
# a = [10,20,30,40,50,60]
# a.remove(a[2])
# print(a)


# # delete the value  present in (-5th to -1st) index in the list
# a= [10,20,30,90,10,10,40,60,80,100]
# del (a[-5:-1])
# print(a)

#
# b = [10,20,30,90,10,10,40,60,80,100]
# del (b[2:])
# print(b)

# Replace the value 300 into 350 in the list
# a = [100,200,300,400,500,600,700]
# a[2]=350
# print(a)


# a = [10,20,30,90,10,10,40,50]
# a.append(70)
# print(a)

# Add a value 50 in the 2nd index and display the list after adding.
# a = [10,20,30,90,10,10,40,50]
# a.insert(2,50)
# print(a)
#
# a=[0,20,30,90,10,10,40,5]
# b=[100,200,300]
# a.extend(b)
# print(a)


# Description : find the maximumand min value in the list
# a = [10,20,30,90,10,10,40,50]
# b = ['java','python','selenium','Java','Python','Selenium']
# print(max(a))
# print(min(b))

# count the 10 value present in the list
# a =[10,20,30,90,10,10,40,50]
# i=a.count(10)
# print('count the 10 value present in the list: ',i)

# Reverse the values present in list
# a = [10,20,30,50,90,40,100,60,10,70]
# a.reverse()
# print('Reverse the values present in list:', a)

# Sort the values (Ascending &Descending ) order present in list
# a = [10,20,30,50,90,40,100,60,10,70]
# a.sort()
# print('Ascending order:', a)
# a.sort(reverse=True)
# print('descending order:', a)

# Copy the values in list
#
# a= [10,20,30,90,10,10,40,50]
# co=a.copy()
# print('copied list is:', co)

# # Create a  listswith values and compare the two list
# a = [10, 20, 30, 90, 10, 10, 40, 50]
# b = [30, 40, 50, 60, 80]
# print(a==b)

# Get the each value of list by using  for loop
# List = 105, 205, 305, 405, 505, 605, 705, 805
# for i in range(0,len(List),+1):
#     print(i,'***',List[i])

# enumerate
L = [105, 202, 305, 405, 505, 605, 705, 805]
res=[]
for i,j in enumerate(L):
    if j%2==0:
        res.append(j)
print(res)
print(respond)

















