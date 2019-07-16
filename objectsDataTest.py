#Answer these 3 questions without typing code. Then type code to check your answer.
#What is the value of the expression 4 * (6 + 5)
import math

# #What is the value of the expression 4 * 6 + 5 
valueA = 29

print('The answer to the expression above is: %s'%valueA)
# #What is the value of the expression 4 + 6 * 5 
valueB = 34

print('The answer to the expression above is: %s'%valueB)
# What is the type of the result of the expression 3 + 1.5 + 4?
print('What is the type of the result of the expression 3 + 1.5 + 4?')

expression= 3 + 1.5 + 4

print(expression)

print('The answer would be: %s' %type(expression))

# What would you use to find a number’s square root, as well as its square?
print('Find the square root of: 89')

valueC = 89

sqrtValueC = math.sqrt(valueC)

print('The square root of 89 is: %s' %sqrtValueC)
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
# # Print out 'e' using indexing
print(s[1])
# Reverse the string 'hello' using slicing:
print(s[::-1])

# Given the string hello, give two methods of producing the letter 'o' using indexing.

# s ='hello'
# # Print out the 'o'
# # Method 1:
print('Printing out the letter o using 1 methond: %s' %s[4])

# # Method 2:
print('Printing out the letter o using second methond: %s' %s[-1])

# Build this list [0,0,0] two separate ways.
# # Method 1:
list1=[0,0,0]

print(list1)

# # Method 2:
list2=[]

list2.append(0)
list2.append(0)
list2.append(0)
print(list2)
# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]

print(list3)

print('Reassigning hello to be goodbye')

list3[2][2] = 'goodbye'

print(list3)

# Sort the list below:
list4 = [5,3,4,6,1]
print(list4)
list4.sort()
print(list4)

# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
# # Grab 'hello'
print(d.values())

#Alternative Method actuallying using indexing

print(d['simple_key'])

d2 = {'k1':{'k2':'hello'}}
# # Grab 'hello'
print(d2)

print(d2['k1']['k2'])
# # Getting a little tricker
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])
# #Grab hello
# # This will be hard and annoying!
d4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d4['k1'][2]['k2'][1]['tough'][2][0])

# Use a set to find the unique values of the list below:

list5 = [1,2,2,33,4,4,11,22,3,3,2]

print(set(list5))