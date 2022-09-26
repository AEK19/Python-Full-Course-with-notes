# phrase = "Giraffe Academy"
# print(phrase.replace("Giraffe", "Elephant"))

# print(10 % 3)
# ---------------------------------------------------------->
# my_num = -5
# print(pow(my_num))
# pow(3,2) the first number is 3and it is raised to 2 so answer is 9
# print(round(3.2)) you get the answer of 3 but if you do '3.7' you get the ans of 4
from math import *
# ------------------------------------------------------------------->
# the floor function just chops off the decimal point ie: 3.7 they just print out 3 to get rid of decimal
# print(ceil(3.2))
# ceil always rounds number up to nearest whole number
# print(sqrt(36))
# ------------------------------------------------------->
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)
# # when you add the variable 'name' then = ... its telling users your name is ....
# # input helps with making things more interactive for users :)
# --------------------------------------------------------------->
# BELOW WILL BE THE FIRST PROJECT 'THE MATH CALCULATOR' :0

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
#
# print(result)
# the problem with the code above is that python will translate the output into a string
# you have to change from string to numbers that is the goal in this
# you add the 'int' in front of 'num1' and 'num2' so python knows to covert from string to number
# when you try to add decimals to the input it outputs an error because the 'int' function is looking for a whole number
# replace 'int' with 'float' to get numbers with decimals to print out properly

# Basic Mad Libs Game below

# color = input("Enter a color: ")
# plural_noun = input("Enter a Plural Noun: ")
# celebrity = input("Enter a celebrity: ")
#
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# friends = ["C", "T", "S", "L", "M"]
# friends[1] = "A"
# print(friends[1:3])
# with lists you can have strings, booleans, and numbers and Python ignores these different data types
# for an index python uses 0 1 2 3 4... the 0 would be 'Cam' in this example
# as soon as you use '[]' Python knows that you are requesting an index find within a list
# if you use -1 inside the bracket, Python outputs a the last thing within a list
# back of the list index starts at -1
# front of the list index starts at 0
# if you want to select items within a list after a certain point you do [x number:] and this grabs the..
# ... item all the way until end of list
# if you do [1:3] it cuts off at certain point depending on index value you provide
# you can also update a list by assigning variable like this friends[1] = "name" and Python will update it

# List functions below


# lucky_numbers = [4, 8, 1, 3, 90, 28]
# friends = ["C", "T", "S", "L", "M"]
#
# friends2 = friends.copy()
#
# print(friends2)

# if a specific element is within a list you do print(friends.index("T") and it returns back the # of index it is in
# if you do friends.count("T") it shows the number of times that name is in the list
# if you do friends.sort() python will output the list in ascending order
# to reverse a list friends.reverse
# copy function of a list is when you add a new variable to copy the same exact list

# --------------------------------->
#  tuple(sub category of lists)
# coordinates = (4, 5)
# coordinates[1] = 10
# print(coordinates[1])
# you cannot modify tuples (meaning you can't add, erase, delete, any information that is already within a tuple)
# to access tuple use an []
# you can have tuples as lists but tuples are for data that will not be changed
# ------------------------------------------------->
# Functions
# functions are one of the core concepts in Python
# to start a function out, you start with 'def'
# you can do say hi with an underscore or without one because its a simple two word function, best to practice with '_'
# text-editor in Python will automatically indent after the def function
# anything outside the indent will not be apart of function 
# there's a marker on the left of the code that will tell you if it is in the function or outside of function
# to execute code there is something called 'calling' to a function so it can operate
# to operate a function you use the variable after the 'def' then you do open parenthesis
# name functions in all lower case
# two or more words use an underscore in between
# parameters are pieces of information we give to the function
# if you don't want to put the string inside the function you can do str(age) within print function to convert it
# any type of data is accepeted within functions
# ------------------------------------------------->
# def say_hi(name, age):
#     print("Hello " + name + ", you are " + str(age))
#
# say_hi("John Wick", 22)
# say_hi("Johnny Dang", 32)
# ------------>

# Return
# the return statement works for
# can't put any code after return statement
# one trick i struggled with lol is that make sure indent is fixed meaning that the 'def' is all the way to the left
# -------->

# def cube(num):
#     return num*num*num
#
# result = cube (4)
# print(result)
# -------->

# IF statements

# if statements are similar to talking about whether a statement is either true or false
# when you type in 'False' the ouput is blank, but if you type in 'True' there will be an output of the print
# the keyword 'else' means in statements as otherwise
# when you add in 'else' now you can print the false statement that is read within the print
# you can write about of 'if' statements to check the combinations of the 'True' and 'False' variables
# the keyword 'or' is for multiple combinations within an 'if' statement
# changing the 'True' or 'False' value in the beginning will determine the outcome
# in the 'and' statements both conditions have to be true
# to add to the condition there is a statment called elseif or 'elif'
# the keyword 'not' negates anything within the open parenthesis
# I made the mistake by not changing some of the keywords for the if statments, so make sure they are all cleaned up

# -------->
# is_male = True
# is_tall = False
# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not (is_male) and is_tall:
#     print("You are not are male but are tall")
# else:
#     print("You either are not male or not tall or both")
# --------->
# If statements & Comparisons
# the following example below will be use 'if' statements to see which is the largest # out of the three
# you can see the comparisons using the 'and' keyword
# > sign that means greater than
# when you use >= it is greater than or equal to... for <= this is less than or equal to
# this is technically a boolean because you are trying to get 'True' or 'False' by using symbols as comparisons
# if the statement is true for num1 you put 'return num1'
# the same concept is applicable to strings
# '==' checks to see if values are equal to each other

# ------->
# def max_num(num1, num2, num3):
#     if num1 >= num2  and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(3,4,5))
# ------>

# 'Better' Calculator

# add 'float' in front of input to convert any possible float values
# the values num1 num2 and op show that we will need two numbers and an operator to make a proper calculator
# if statements will better define the conditions we need so the 'op' or operator functions well with
# if the user does not want to use the operators stated below, use the 'else' condition to output invalid operation
# i am using the round function so I do not have to see so many decimals
# also do not forget to name your variables
#
# num1 = float(input("Enter your first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter your first number: "))
# ------->
# if op == "+":
#     print(round(num1 + num2))
# elif op == "-":
#     print(round(num1 - num2))
# elif op == "/":
#     print(round(num1 / num2))
# elif op == "*":
#     print(round(num1 * num2))
# else:
#     print("Invalid operator")

# -------->

# Dictionary

# Dictionary is a special feature in Python that allows us to store information
# dictionaries normally have words and definitions for programming we will use keywords as words
# Jan -> January
# Mar -> March
# use curly brackets
# avoid duplicate keys
# use these '[]' to put string value to get values
# another option is to do monthConversions.get() instead of brackets
# in the 'get' function you can specify the default and have an output of 'none' if value input is not in dictionary
# to get a different value from 'none' you can do this: , "Not a valid Key"))
# key values below can be numbers
# ------->

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }
#
# print(monthConversions.get("Luv", "Not a valid Key"))
# ------>
# While Loop
# while loops are defined as code that repeats through conditions until a condition is false
# if condition is false the while loop will not work
# one instance is to check condition before running code, analyze anythign wrong, then analyze code
# ----->
# i = 1
# while i <= 10:
#     print(i)
#     i = i +1
# print("Done with loop ")
# -------->
# Guessing game will be Below
# In this game users will be asked to guess a secret word, if they guess it incorrectly the game will prompt them
# ... to enter it again
# goal is to specify a looping condition
# the 'guess' that user input whether right or wrong is stored in the variable 'guess' then you check to see if the
# ... guess is equal to the secret word
# if guess is correct we are going to break out of loop
# adding a 'guess limit' sets a limit on the loop
# adding a 'guess count' counts the number of times someone guesses on the loop
# add the boolean 'out of guesses' to explain to users they
# if out of guesses is 'True' then they lost the game vice versa if they are 'False'
# now we use the 'if' condition to see if user has used all their guesses
# if guess count is less than guess limit they still have some guesses left
# implement the 'else' condition if they have more guesses to show that it is true they cannot make any more attempts
# add the 'and not' condition to show that they are not out of guesses yet and the loop continues
# the 'if' condition is added in the end to show the loop result if out of guesses and the 'else' condition is added
# ... if they win
# remember to indent
# ------>
# secret_word = "zebra"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if guess_count <  guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print("Out of Guess, You Lose! ")
# else:
#     print("You Win! ")
# ----------------------------------------------->
# For Loops
# for loops help us loop over different collections
# for each letter in Zebra academy the user wants to print out 'letter'
# with the range an index you use 'len' to measure the length of the list, but the range is from 0 and the number of
# ... friends
# the print function with 'friends' and 'index' allows you to print out each individual in the list
# 'for' loops work in arrays and 'strings'
#
# friends = ["Jane", "Peter", "Michael"]
#
# for index in range(len(friends)):
#     print(friends[index])
# ---------------------------------------->
# Exponent Function
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
# print(raise_to_power(3, 2))

# 2D Lists & Nested Loops
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
#
# for row in number_grid:
#     for col in row:
#         print(col)
# ---------------------------------->
# Translator
# going to be looping through the 'phrase'
# python can check to see if something is in something else

# def translate(phrase):
#     translation = ""
#     for letter in "AEIOUaeiou":
#         translation = translation + "t"
#     else:
#         translation = translation + letter
#     return translation
#
# print(translate(input("Enter a phrase: ")))
# --------------------------------------------->

# Comments
# you can make multiple line comments using "'" which are single quotes
''''''''
# writing under these single quotes gives you comments but you have to send them by putting "'" under this line
''''''''
# TRY EXCEPT BLOCK
# this except will allow programs to try out code
# this is a great tool to use to try new codes
# don't forget colons
# the underline under 'except' is because it is too broad of a clause
# there are multiple ways you can
# can fix the below issue by saying 'ZeroDivisionError'

# we can store this error as a variable using 'as' and 'err
# best practice in python is to use the specific error notes similar to 'ZeroDivisionError'
# you don't need a colon before the 'except'

# try:
#     answer = 10 / 0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# ---------------------------------------------------->
# Python read files
# first type 'open' then if there is a file on the left of the directory, you type the name of the file as str
# this will be an example because I haven't imported a file ... oops :(
# open("employees.txt" , "r") ---> this is only if you want to read the file
# open("employees.txt" , "w") ----> this means you can write in the file
# open("employees.txt" , "a") ----> this means you can 'append' which means add new info to file
# open("employees.txt" , "r+") ----> this gives you all the power with reading and writing within a file

# make sure to close file using variable.close()
# surprisingly there are booleans in this as well using print(variable.readable())
# it will output 'True' if you selected r before , but if not the output in console will be 'False'
# to access lines do print(variable.readline()) and this picks the first line automatically


# to access speciic lines do print(variable.readlines([1])) this is specifically within the index
#

# open()

# ---------------------------------------------->

# Module
# modules are just python files that we can import into our current python file
# in this example lets say we do have an external file to import from we would do ... import my_variable
# after you do this... you can do print(my_varaible.whatever_file_you_want_import)
# you can find more modules at  docs.python.org or you can use 'External Libraries' on the side (then hit 'Lib' after)
# some files are built in some are external


# Multiple Choice Quiz
# one of the errors I had before changing it was that you need to name the file EXACTLY how it is so the import works
# for example you may get the message ModuleNotFoundError: No module named 'question' so i switched the file name to
# ... 'Question'
# I spent about 15 mins trying to figure out why my rule wasn't working, but all i had to do was spell __init__ correct

from Question import Question
#
# questions_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are Tangerines?\n(a) Teal\n(b) Purple\n(c) Orange\n\n",
#     "What color are strawberries?\n(a) Red\n(b) Black\n(c) Blue\n\n"
]
#
# questions = [
#     Question(questions_prompts[0], "a"),
#     Question(questions_prompts[1], "c"),
#     Question(questions_prompts[2], "a"),
# ]
#
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#         print("You got " + str(score) + "/" + str(len(questions)) + "correct")
# run_test(questions)


# Another shortcut to create comments if you are on a mac is to use 'command + /' and this automatically

