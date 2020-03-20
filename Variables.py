_author_ = "raj"
greeting = "Raj"
_myName = "Anba"
Greeting = "Hello"
#same varible with different case will act as different & stored different in memory
print(Greeting+' '+ greeting)

age = 30
print(age)

#Below will throw an exception-"can only concatenate str (not "int") to str"
#print(greeting+age)

a=12 #Integer(Whole number) variable
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b) #This operator returns floating number
print(a // b) #This operator returns integer number
print(a % b)

#Adding few complex math
#Operator precedence starts with division, multiplication,subtraction,addition
#12 + 3/3 - 4 *12
#12 + 1 - 48
#-35.0
print(a + b / 3 -4 * 12)

#Use braces in order to change the precedence
print((((a+b)/3)-4)* 12)

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
#If you use negatice number then it will read from the back and print the value
print(parrot[-1])
#You can use colon to select range of characters from a string
print(parrot[0:6])
#if your not specifying any start or end of the range by default it takes start and end of string character ranger
print(parrot[:6])
print(parrot[6:])

#Below double colon will start from range 1 and skips 4 character from that
number ="9,223,372,036,854,775,807"
print(number[1::4])

#You can mulitply string in pyhton
print("Hello " * 5 )
#Find substring from a String . It will return true or false
today = "Friday"
print("day" in today)




