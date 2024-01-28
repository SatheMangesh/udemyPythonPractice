"""
09-Objects and Data Structures Assessment Test

Run below programs saperately as the variable names are same in few tests

"""

"""
Numbers: Simple Arithmetic
Write an expression that equals 100. 
"""

from os import system


print(200-100)
print(25*4)
print(50+50)
print(200/2)

"""
Use what you know about the print() function to print out the phrase "Hello World" . Make sure your capitalization and spacing match.
"""

print("Hello World")


"""
String Indexing
Write a string index that returns just the letter 'r'  from 'Hello World' .

For example, 'Hello World'[0]  returns 'H' 
"""

mystr = 'Hello World'
print(mystr[8])

"""
String Slicing
Use string slicing to grab the word 'ink'  from inside 'tinker' 

For example, 'education'[3:6]  returns 'cat' 

Remember that when slicing you only go up to but not including the end index.
"""

mystring = 'tinker'
print(mystring[1:4:])

""""
Print Formatting
Write an expression using any of the string formatting methods we have learned (except f-strings, see note below) to return the phrase 'Python rules!' 

For example, these phrases both return 'I like apples' :

'I like %s' %'apples'
'I like {}'.format('apples')
Your solution should be entered on one line. You can not use variable names, only the strings themselves.

"""

print('Python %s!' %'rules')

print('Python {}!'.format('rules'))

value1 = 'mysatr'
print(f'mystring is {value1}')

""""
Lists
Create a list that contains at least one string, one integer and one float.

For example:

[1, 'two', 3.14159] 

Note that the order and number of items doesn't matter. 
"""

mystring = ['a',100,67.88]

print(mystring)
"""
Dictionaries
Create a dictionary where all the keys are strings, and all the values are integers.

For example:

{'Monday':19, 'Tuesday':20}

Just write the dictionary on a single line, don't assign a variable name to the dictionary.
"""


mydict = {'planets':9, 'constolessions' : 27, 'signs':12}

print(mydict)
"""
Sets
Write an expression that would turn the string 'Mississippi'  into a set of unique letters.

For example:

set('Parallel') 

would return the set {'P', 'a', 'e', 'l', 'r'}

You should only write one line of code for this. Do not assign a variable name to the set.
"""
system('cls')

myset = set('Mississippi')
print(myset)

"""
File I/O
This exercise will require several lines of code.

Write a script that opens a file named 'test.txt' , writes 'Hello World'  to the file, then closes it.

For example, the following code opens a file called 'myfile.txt' , writes 'This is my file' , and closes it:

x = open('myfile.txt', 'w')
x.write('This is my file')
x.close()
"""

myfile = open('test.txt','a')
myfile.write('Hello World\n on newline')
#myfile.write('\n')
myfile.close()

myfileread = open('test.txt','r')
print(myfileread.read())
myfileread.close()

"""
Answer these 3 questions without typing code. Then type code to check your answer.

What is the value of the expression 4 * (6 + 5)

What is the value of the expression 4 * 6 + 5 

What is the value of the expression 4 + 6 * 5 
"""


print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5 )

"""
What is the type of the result of the expression 3 + 1.5 + 4?

"""

print(type( 3 + 1.5 + 4)) #expecting float

"""
What would you use to find a number’s square root, as well as its square?
"""
import math


number = 4
print(f'Square root of {number} is {math.sqrt(number)}')
print(f'Square of {number} is {number**2}')

"""
Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below
:"""


mystring = 'hello'
print(mystring[1])

"""Reverse the string 'hello' using slicing:"""

myrevstring = 'mangesh'
print(myrevstring[::-1])

"""
Given the string hello, give two methods of producing the letter 'o' using indexing.
"""

mystring = 'hello'

print(f'first method is {mystring[len(mystring)-1]}')
print(f'second method is revering {mystring[-1]}')

""" **** check solution
Build this list [0,0,0] two separate ways.
"""

methodone_list = [0,0,0]
mylist = []

for item in range(3):
    mylist.append(0)

print(mylist)


"""
Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 = [1,2,[3,4,'hello']]

"""

list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'goodbye'

print(list3)

"""
Sort the list below:
list4 = [5,3,4,6,1]
"""


list4 = [5,3,4,6,1]
list4.sort()
print(list4)

"""
Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}

"""



d = {'simple_key':'hello'}

print(d['simple_key'])

d = {'k1':{'k2':'hello'}}

print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#print(type(d))
level1 = d['k1']
#print(level1)
#print(type(level1)) # its a list of directories
level2 = level1[0]['nest_key'][1][0]
print(level2)


def myprint(datapassed):
    print(datapassed)
    print(type(datapassed))
    return datapassed

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
itr1 = myprint(d['k1'])
itr2 = myprint(itr1[2])
itr3 = myprint(itr2['k2'])
itr4 = myprint(itr3[1])
itr5 = myprint(itr4['tough'])
itr6 = myprint(itr5[2][0])

"""
Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
"""

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

"""
What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)
2 > 3

"""
system('cls')
print(2 > 3) #F
print(3 <= 2) #f
print(3 == 2.0) #F
print(3.0 == 3) #T
print(4**0.5 != 2) #F


"""
What is the boolean output of the cell block below?
"""

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?

print(l_one[2][0] )  # evaluates to 3
print( l_two[2]['k1'])  # evaluates to 4
#Answer is False
print(l_one[2][0] >= l_two[2]['k1'])  