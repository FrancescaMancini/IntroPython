# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 17:16:51 2017

@author: User
"""

text = "Hello world"
integer = 1
my_float = 2.35

print(text) # returns variable value
print(integer)
print(my_float)

# arithmetics
x = 5
y = 6

print(x + y)

z = x + y
print(z)

print(x - y)
print(x * y)
print(x / y)
print(x ** y)
print(x % y)

# Strings
print(text)
print(len(text)) # returns number of chanracters in string
print(text.upper()) # capitalise
print(text.lower()) # opposite

fruit = "Apples" + " " + "Bananas" # creates character string not vector!
vegetable = "Potatoes"

shoppinglist = fruit + " " + vegetable

print(shoppinglist)
print(shoppinglist[2]) # indexing

print(text[0])
print(text[2])
print(text[1:4])
print(text[-1])

n = len(text)
print(text[n-1])

# Lists
shopping = ["Apples","Potatoes","Bananas","Biscuits"] # creates a vector
print(shopping)
print(shopping[1]) # returns second element of the vector

print(len(shopping)) # returns number of elements in list

shopping.append("Strawberries") # increases list by one element
print(shopping)
print(len(shopping))

shopping.extend(["Gravy","Lemonade"]) # extends the list with another list
print(shopping)
print(len(shopping))

shopping.sort() # sorts list, in this case alphabetically
print(shopping)
print(len(shopping))

shopping.reverse() # reverts the order
print(shopping)
print(len(shopping))

# Loops
for i in range(1,10): # prints variable i which takes values from 1 to 9
	print(i)
    
for i in range(1,10,2):
	print(i)


for item in shopping: # loops through elements of a list (no need for the range())
	print(item)

for item in shopping:
	length = len(item)
	char = item[0]
	print("I need " + item + ". This word is " + str(length) + " characters long and begins with " + char)

for item in shopping: # if statement
	if item[0] == "B":
		print(item)

for item in shopping:
        if item[0] == "B":
                print(item + " begins with B")
        elif item[0] == "A":
		          print(item + " begins with A")
        else:
		          print(item + " doesn't begin with B or A") 

# syntax
for item in shopping:
    if item[0] == "B":
        print(item)
    elif item[0] == "A":
        print(item)
        


