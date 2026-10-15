###TOC

#List Comprehension



##########################################################

#Python - List Comprehension

# A list comprehension is a concise way to create lists. 
# It is similar to set builder notation in mathematics.
# It is used to define a list based on an existing iterable object, 
# such as a list, tuple, or string, and apply an expression to each element in the iterable.


#new_list = [expression for item in iterable if condition]

# squares = [x * x for x in range(1, 11) if x % 2 == 0] 
# print(squares)  # [4, 16, 36, 64, 100]

###############################################################

##Operators in python

# types of operator

# 1. Arithmetic operator
# 2. logical operator
# 3. comparision operator
# 4. membership operator
# 5. bitwise operator
# 6. identity operators
# 7. assignment operator
# 8. terinary operator


# 1.Arithmetic operators:
# a=10, b=20
# +	Addition	a + b = 30
# -	Subtraction	a - b = -10
# *	Multiplication	a * b = 200
# /	Division	b / a = 2
# %	Modulus	b % a = 0
# **	Exponent	a**b =10**20
# //	Floor Division	9//2 = 4

# 2.logical operators:

# FAlSE: 0,{},[],()
# #

# Logical "and" Operator Truth Table

# For the compound Boolean expression to be True, both the operands must be True. 
# If any or both operands evaluate to False, the expression returns False.

# a	b	a and b
# F	F	F
# F	T	F
# T	F	F
# T	T	T

#Logical "or" Operator Truth Table

#In contrast, the or operator returns True if any of the operands is True. 
# For the compound Boolean expression to be False, both the operands have to be False.

# a	b	a or b
# F	F	F
# F	T	T
# T	F	T
# T	T	T

#Logical "not" Operator
#This is a unary operator. 
# The state of Boolean operand that follows, is reversed. 
# As a result, not True becomes False and not False becomes True.

# a	not (a)
# F	T
# T	F

# 3. comparision operator:

# Comparison operators in Python are very important in Python's conditional statements 
# (if, else and elif) and looping statements (while and for loops)

#  >, <, >=, <=, ==, !=

# comparison of int and float
# a= 10 b= 10.0 a>b is False
# a= 10 b= 10.0 a<b is False
# a= 10 b= 10.0 a==b is True
# a= 10 b= 10.0 a!=b is False


# 4. membership operators:

# Python has two membership operators: in and not in

# This in and not operators can only used on collection data types.

# IN operator:
# The "in" operator is used to check whether a substring is present in a bigger string, 
# any item is present in a list or tuple, or 
# a sub-list or sub-tuple is included in a list or tuple.

# var = "TutorialsPoint"
# a = "P"
# b = "tor"
# c = "in"
# d = "To"
# print (a, "in", var, ":", a in var)
# print (b, "in", var, ":", b in var)
# print (c, "in", var, ":", c in var)
# print (d, "in", var, ":", d in var)

# Output:
# P in TutorialsPoint : True
# tor in TutorialsPoint : True
# in in TutorialsPoint : True
# To in TutorialsPoint : False 

# Not IN operator:

#The "not in" operator is used to check a sequence with the 
# given value is not present in the object like string, list, tuple, etc.

# var = "TutorialsPoint"
# a = "P"
# b = "tor"
# c = "in"
# d = "To"
# print (a, "not in", var, ":", a not in var)
# print (b, "not in", var, ":", b not in var)
# print (c, "not in", var, ":", c not in var)
# print (d, "not in", var, ":", d not in var)

#output:
# P not in TutorialsPoint : False
# tor not in TutorialsPoint : False
# in not in TutorialsPoint : False
# To not in TutorialsPoint : True

# Membership Operator with Lists and Tuples

# You can use the "in/not in" operator to check the membership of an item in the list or tuple.

# var = [10,20,30,40]
# a = 20
# b = 10
# c = a-b
# d = a/2
# print (a, "in", var, ":", a in var)
# print (b, "not in", var, ":", b not in var)
# print (c, "in", var, ":", c in var)
# print (d, "not in", var, ":", d not in var)

# Output: 
# 20 in [10, 20, 30, 40] : True
# 10 not in [10, 20, 30, 40] : False
# 10 in [10, 20, 30, 40] : True
# 10.0 not in [10, 20, 30, 40] : False

# Cannot find sub-string in list/tuples/set

# var = ["Hello", "world"]
# a="hel"
# print(a in var)

# Output: False

# However, if you try to check if two successive numbers are present in a list or tuple, 
# the in operator returns False. 
# If the list/tuple contains the successive numbers as a sequence itself, then it returns True.

# var = (10,20,30,40)
# a = 10
# b = 20
# print ((a,b), "in", var, ":", (a,b) in var)
# var = ((10,20),30,40)
# a = 10
# b = 20
# print ((a,b), "in", var, ":", (a,b) in var)

# Output:
# (10, 20) in (10, 20, 30, 40) : False
# (10, 20) in ((10, 20), 30, 40) : True

# Membership Operator with Sets:

# var = {10,20,30,40}
# a = 10
# b = 20
# print (b, "in", var, ":", b in var)
# var = {(10,20),30,40}
# a = 10
# b = 20
# print ((a,b), "in", var, ":", (a,b) in var)


# 5. bitwise operator:

# Python bitwise operators are normally used to perform bitwise operations on integer-type objects.

# The following are the bitwise operators in Python -
# Bitwise AND Operator(&)
# Bitwise OR Operator(|)
# Bitwise XOR Operator(^)
# Bitwise NOT Operator(~)
# Bitwise Left Shift Operator(<<)
# Biwtise Right Shift Operator(>>)


# Bitwise AND Operator (&):

# 0 & 0 is 0
# 1 & 0 is 0
# 0 & 1 is 0
# 1 & 1 is 1

# a=60
# b=13
# print ("a:",a, "b:",b, "a&b:",a&b)

# Python Bitwise OR Operator (|)

# a=60
# b=13
# print ("a:",a, "b:",b, "a|b:",a|b) -->a: 60 b: 13 a|b: 61
# print ("a:", bin(a))  -->a: 0b111100
# print ("b:", bin(b))  -->b: 0b1101


# Python Bitwise NOT Operator (~)
# This operator is the binary equivalent of logical NOT operator. 
# It flips each bit so that 1 is replaced by 0, and 0 by 1, and returns the complement of the original number.


#Python Bitwise XOR Operator (^)

# The term XOR stands for exclusive OR. 
# It means that the result of OR operation on two bits will be 1 if only one of the bits is 1.

# 0 ^ 0 is 0
# 0 ^ 1 is 1
# 1 ^ 0 is 1
# 1 ^ 1 is 0

# a=60
# b=13
# print ("a:",a, "b:",b, "a^b:",a^b)

# print(1^0^0)  --> 1
# print(1^1^0)  --> 0

# Python Bitwise Left Shift Operator (<<)

# we have to shift the bites to left 
# all the of bytes of a number is shifted to given number of times to left

# a=60
# print ("a:",a, "a<<2:", a<<2) --> a: 60 a<<2: 240

# How does this take place? Let us use the binary equivalent of 60, and perform the left shift by 2

#0011 1100
# <<
#     2
# -------------
# 1111 0000

# Convert the binary to integer. It is 240.

#>>> int('11110000',2)
# 240

# Python Bitwise Right Shift Operator (>>)

# Right shift operator shifts least significant bits to left by the 
# number on the right side of the ">>" symbol.
#  Hence, "x >> 2" causes two bits of the binary representation of to left.

# a=60
# print ("a:",a, "a>>2:", a>>2) --> a: 60 a>>2: 15

#Manual right shift operation on 60 is shown below −

#    0011 1100
#    >>
#    2
#    -------------
#    0000 1111

# Use int() function to covert the above binary number to integer. It is 15.

# >>> int('00001111',2)
# 15

# 6. identity operators:

# two types of identity operators:

# 'is' Operator
# 'is not' Operator

# The 'is' operator evaluates to True if both the operand objects share the same memory location
# The memory location of the object can be obtained by the "id()" function.
# If the "id()" of both variables is same, the "is" operator returns True.

# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 4, 5]
# c = a

# Comparing and printing return values
# print(a is c)
# print(a is b)

# Printing IDs of a, b, and c
# print("id(a) : ", id(a))
# print("id(b) : ", id(b))
# print("id(c) : ", id(c))

# Output:
# True
# False
# id(a) :  140114091859456
# id(b) :  140114091906944
# id(c) :  140114091859456

# The 'is not' operator evaluates to True if both the operand 
# objects do not share the same memory location or both operands are not the same objects.

# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 4, 5]
# c = a

# # Comparing and printing return values
# print(a is not c)
# print(a is not b)

# # Printing IDs of a, b, and c
# print("id(a) : ", id(a))
# print("id(b) : ", id(b))
# print("id(c) : ", id(c))

# Output: 
# False
# True
# id(a) :  140559927442176
# id(b) :  140559925598080
# id(c) :  140559927442176

# memory is shared with immutable collection data types, so we get true for identity operator.

# print("for the String")
# a = 'Hello' 
# b = 'Hello'

# print(a is b)

# print(f"ID of a is {id(a)}")
# print(f"ID of b is {id(b)}")


# print("for the List")
# c = [1,2,3]
# d = [1,2,3]

# print(c is d)

# print(f"ID of c is {id(c)}")
# print(f"ID of d is {id(d)}")


# print("for the Set")
# x = (10,20,30)
# y = (10,20,30)

# print(x is y)

# print(f"ID of x is {id(x)}")
# print(f"ID of y is {id(y)}")

# print("for the Dictionary")
# s = {'a':'11', 'b':'22','c':'33'}
# t = {'a':'11', 'b':'22','c':'33'}

# print(s is t)

# print(f"ID of s is {id(s)}")
# print(f"ID of t is {id(t)}")


# print("for the integer")
# ax= 99
# bx = 99

# print(ax is bx)

# print(f"ID of ax is {id(ax)}")
# print(f"ID of bx  is {id(bx)}")


# 7. assignment operator:

#'=' is used as assignment operator

# ex: a=5

# +=, -=, %=, /=, //=, **=

# 8. terinary operator

# true_value if condition else false_value

# var_1 = 10
# var_2 = 45
# result = "var_1 is less than var_2" if var_1 < var_2 else "var_2 is less than var_1" 
# print(result)

# The ternary operator can be used with different data types ?

# Using tuples
# Using dictionary
# Using lambda

# (false_value, true_value)[condition] # Tuples

# var_1 = 15
# var_2 = 0
# result = ("var_1 and var_2: False", "var_1 and var_2: True")[var_1 and var_2]
# print(result)

# {True: true_value, False: false_value}[condition] # dictionary 

# var_1 = 1
# var_2 = 0
# result = {True: "var_1 or var_2: True", False: "var_1 or var_2: False"}[var_1 or var_2]
# print(result)

# (lambda: false_value, lambda: true_value)[condition]()  # Lambda

# We can also use the ternary operator with lambda. This is similar to a tuple where 
# false_value is at 0 index and true_value at 1. If the condition is True it will return 
# the index 1 value. Otherwise, the value corresponds to the 0 index.

# var_1 = 8
# result = (lambda: "False", lambda: "True")[var_1 < 0]()
# print(result)

# For else, while else, version control, git, github.

###############################################################################
# for...else

# example 1: Loop completes naturally (Else executes)

# numbers = [1, 2, 3]

# for num in numbers:
#     print(f"Processing {num}")
# else:
#     print("Loop finished completely without hitting a break!")

# example 2: Loop gets interrupted (Else is skipped)
# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     print(f"Processing {num}")
#     if num == 3:
#         print("Break triggered!")
#         break
# else:
#     print("This will not print because the loop broke.")

# Practical case: searchin an item with a flag

# items = ["apple", "banana", "cherry"]
# search_target = "orange"

# for item in items:
#     if item == search_target:
#         print(f"Found {search_target}!")
#         break
# else:
#     # This runs only if the loop searched everything and didn't find the item
#     print(f"Could not find {search_target} in the list.")

####################################################################################################
# While...else

#Example 1: Loop completes naturally (Else executes)

# count = 1

# while count <= 3:
#     print(f"Count is {count}")
#     count += 1
# else:
#     print("Loop condition became False. Else block executed!")

#output:
# Count is 1
# Count is 2
# Count is 3
# Loop condition became False. Else block executed!

# Example 2: Loop gets interrupted (Else is skipped)

# count = 1

# while count <= 5:
#     print(f"Count is {count}")
#     if count == 3:
#         print("Break triggered!")
#         break
#     count += 1
# else:
#     print("This will not print because the loop broke.")

#output:
# Count is 1
# Count is 2
# Count is 3
# Break triggered!

#Practical Use Case: User Input Validation

# attempts = 3
# correct_password = "secure123"

# while attempts > 0:
#     user_input = input(f"Enter password ({attempts} attempts left): ")
    
#     if user_input == correct_password:
#         print("Access Granted!")
#         break  # Skips the else block
        
#     print("Incorrect password.")
#     attempts -= 1
# else:
#     # This runs only if the user runs out of attempts (attempts becomes 0)
#     print("Account locked. Too many failed attempts.")


####################################################################################################
# IN built method()

# Case Converston 


# # upper(): Converts lowercase letters in string to uppercase.

# text = "hello world"
# print(text.upper())  # Output: HELLO WORLD


# # lower(): Converts all uppercase letters in string to lowercase.

# text = "HELLO WORLD"
# print(text.lower())  # Output: hello world

# # swap-case(): Inverts case for all letters in string

# text = "Python Programming"
# print(text.swapcase())  # Output: pYTHON pROGRAMMING

# # capitalize(): Capitalizes first letter of string

# text = "hELLO wORLD"
# print(text.capitalize())  # Output: Hello world

# # title(): Returns "titlecased" version of string, that is, all words begin with uppercase 
# # and the rest are lowercase.

# text = "welcome to python programming"
# print(text.title())  # Output: Welcome To Python Programming


# Split():
# The Python String split() method splits all the words in a string separated by a specified separator.
# This separator is a delimiter string, and can be a comma, full-stop, space character or 
# any other character used to separate strings.

# text = "apple,banana,cherry,date"
# print(text.split(",", 2))
# # Output: ['apple', 'banana', 'cherry,date']

#Count():

# The python string count() method is used to count the number of non-overlapping occurrences of 
# the substring that is specified as the function's parameter.

# Syntax: str.count(sub, start= 0,end=len(string))


# str = "Hello! Welcome to Tutorialspoint.";
# substr = "i";
# print("The number of occurrences of the substring in the input string are: ", str.count(substr, 3, 30))


# index():
# The python string index() method is used to return the index of the input 
# string where the substring is found.

# syntax: str.index(str, beg=0, end=len(string))

# str1 = "Hello! Welcome to Tutorialspoint."
# str2 = "to";
# result= str1.index(str2, 5)
# print("The index where the substring is found:", result)
# result= str1.index(str2, 18)
# print("The index where the substring is found:", result)

# write a program to write a second oocurance of sub string without using loops

# s='abcdabcdabcdabcd'
# print("The 1st occurence of sub-string ",s.index('a'))
# print("The 2nd occurence of sub-string ",s.index('a',s.index('a')+1))

###################################################################################################

# # # String validation methods

# # isalnum() Method:

# The python string isalnum() method is used to check whether the string consists of 
# alphanumeric characters.

# This method returns true if all the characters in the 
# input string are alphanumeric and there is at least one character. Otherwise, it returns false.

# str = "tutorial123"
# result=str.isalnum()
# print("Are all the characters of the string alphanumeric?", result)

#Output:
# Are all the characters of the string alphanumeric? True

# # isalpha() method:

# it will verify if it has only alphabets then returns true.

# str = "tutorial"
# result=str.isalpha()
# print("Are all the characters of the string alphanumeric?", result)

# # isdigit() method:

# it check given string are numbers or not.

# str = "12345"
# result=str.isdigit()
# print("Are all the characters of the string alphanumeric?", result)

## isspace(), islower() and isUpper()

#####################################################################################################

# # # sorted():

# This method will sort all characters in given string by using the ASCII values
# default sorting is ascending
# return type is list 
# syntax: sorted(varname)

# s= 'Hello'
# print(sorted(s, reverse=True))

# # startswith():

# It gives the bool value true if given substring is at the start if the string.

#syntax: Vname.startswith(substring, arg1, arg2)
#arg1 = start index
#arg2 = end index

# s='Hello, This is a movie starting at 11AM'
# print(s.startswith("hello"))
# print(s.startswith("movie", 17))

# # endswith():

# It gives the bool value true if given substring is at the end if the string.

#syntax: Vname.startswith(substring, arg1, arg2)
#arg1 = start index
#arg2 = end index

# s='We are Future of AI'
# print(s.endswith("AI"))
# print(s.endswith("Future",12,19))

# # # format():

# this method is used for variable substitution in a string
# It is a placeholder ({}) to print the actual meaning.
# syntax: Vname.format(args1,args2,....)

# a=25000
# b='Hari'

# print('{} salary is {} '.format(b,a))

# # # strip():

# The Python string strip() method is used to remove
#  all the specified leading and trailing characters from the beginning and the end of a string.

# syntax: str.strip([chars]);

# str = "0000000this is string 000 example....wow!!!0000000"
# print( str.strip('0'))

# # Lstrip() and Rstrip()

# they remove respective left and right spaces/ char.

s = '   Welcome to home    '

print(s.lstrip())
print(s.rstrip())

# List methods():