#### QUESTION 1 ####
#Create a list of numbers that are less than ten using l_1 and list comprehension
#Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]

print(l_1)

l_1.sort()
print(l_1)

l_1.pop()
print(l_1)

l_1.pop()
print(l_1)


#### QUESTION 2 ####
#Using list comprehension, create a list of names of 4 letters 
#or more and capitalize each name
names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']


names1.remove('bob')
print(names1)
names1.remove('bob')
print(names1)
names1.remove('max')

print(names1)
for name in names1:
    print(name.title())

#### Extra Credit Question 3 ####
#Using list comprehension, create a list of names of 
#4 letters or more and capitalize each name
names2 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']


print(names2)
names2.remove('bob')
names2.remove('max')
names2.remove(2)
names2.remove(3)
names2.remove('bob')
names2.remove(2)
names2.remove(3)
names2.remove(4)
names2.remove(2)
for name in names2:
    print(name.title())