"""
Use for, .split(), and if to create a Statement that will print out words that start with 's':
"""

from os import system


mystatement = 'Print only the words that start with s in this sentence'

splitted = mystatement.split()

for word in splitted:
    if word[0].lower() == 's':
        print(word[0])
        

"""
Use range() to print all the even numbers from 0 to 10.
"""
system('cls')

for number in range(0,11):
    if number % 2 == 0:
        print(number)


"""
Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
"""


blanklist = []

for number in range(1,50):
    if number % 3 == 0:
        blanklist.append(number)
        
print(blanklist)

"""
Go through the string below and if the length of a word is even print "even!"
"""

st = 'Print every word in this sentence that has an even number of letters'

splittedString = st.split()

for word in splittedString:
    if(len(word) %2 == 0):
        print(f'{word} and lenght is {len(word)}')
        
"""
Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
"""
system('cls')

for number in range(0, 100):
    if (number %3 == 0) and (number %5 == 0):
        print("FizzBuzz")
    elif number %3 == 0:
        print("Fizz")
    elif number %5 == 0:
        print("Buzz")
    else:
        pass
    
    
"""
Use List Comprehension to create a list of the first letters of every word in the string below:
"""
system('cls')

st = 'Create a list of the first letters of every word in this string'
splittedStr = st.split()
blanklist = []

for word in splittedStr:
     blanklist.append(word[0])

print(blanklist)