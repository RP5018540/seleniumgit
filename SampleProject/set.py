# Create a new set with values and find the length of it
# set = {10,20,30,90,10,10,40,50}
# set1 ={10,20,30,90,10,10,40,50,'python','java',22.4,True}
# print(len(set))
# print(len(set1))

# Add a value 100 at the last position of tuple
#
# set ={ 10,20,30,90,10,10,40,50 }
# set.add(10)
# print(set)

# set = {10,20,30,90,10,10,40,50}
# set2=(100,200,300)
# set.add(set2)
# print(set)

# # Max and min
# set = {10, 20, 30, 90, 10, 10, 40, 50, 10}
# set1 = {'python','selenium','sql','java'}
# print(max(set))
# print(min(set1))

# Update set by following data {100,200,500}

# set = {10,20,30,40,50,60}
# a={100,200,500}
# set.update(a)
# print(set)

#
#
# set = {10,20,30,40,50,60}
# a=('j'+'greens')
# set.update(a)
# print(set)

# Convert string into set
# i=set('python')
# print(i)

# Convert list into set
# List = ['java','python',20,10,60]
# tuple = (105,205,305,405,505,605,705,805,'java','python',20,10,60)
# i=set(List)
# a=set(tuple)
# print(i)
# print(a)

# To check weather value 200 is present or not in set

#
# set ={ 105,205,305,405,505,605,705,805}
# print(200 in set)
# print(205 in set)

# Create a set with values and compare the another set

# set= {10,20,30,40,50,60}
# set1 = {10,20,30,40,50,60}
# print(set==set1)

# Get the each value of set by using  for loop

# set = {105, 205, 305, 405, 505, 605, 705, 805}
# for i in set:
#     print(i)
#
# Get the each value of tuple by using  Enumarate for loop
set = {105, 205, 305, 405, 505, 605, 705, 805}
for i,val in enumerate (set):

    if val%2==0:
        print(val)
