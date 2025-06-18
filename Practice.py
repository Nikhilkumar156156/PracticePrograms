#1 First

# def calculator(first=int(input("enter a number")),second=int(input("enter sec number"))):
#     c=(input("Enter a for Addition, s for Substraction, d for Divide, m for Multiplication"))
#     if (c =="a"):
#       e = first+second
#       print(e)
#     elif (c == "s"):
#       e = first  -second
#       print(e)
#     elif (c == "d"):
#       e = first / second
#       print(e)
#     elif (c =="m"):
#       e=first*second
#       print(e)
#     else:
#      print("Not a valid input")
# calculator()

#-------------------------------------------------

#2 Second

# a=32
# b=222
# print("A") if a>b else print("=") if a==b else print("B")

#-------------------------------------------------

#3 Third Not working

# def function(f, x):
#     return f(x) + x

# cu = lambda x: x*x*x
# print(function(cu, 1))

#-------------------------------------------------

#5

# def Calculate_Price():
#     Total = 0

#     while True:

#         input_by_user = input("Enter a number to addition or B to exit:")
#         if input_by_user == "B":
#              break
#         elif input_by_user == "b":
#             break
#         try:
#             price = int(input_by_user)
#             Total = Total + price
#         except ValueError:
#             print("Invalid value")
        
#     return Total

# P = Calculate_Price()
# print("Total:", P)

#-------------------------------------------------

# To Find the Factorial- 6

# def factorial(num):
#     number = 1
#     while num > 0:
#         number = num*number
#         num = num - 1
#     return number

# a = factorial(int(input()))
# print(a)

# No. of trailing zeros

# def trailing_zeros(a):
#     zero = 0
#     while a%10 == 0:
#         zero = zero + 1
#         a = a//10
#     return zero
# if __name__ == "__main__":
#     b = trailing_zeros(a)
#     print(b)

#-------------------------------------------------

#Practyice no 7

# usd = 85.79
# inr = 1
# euro = 97.81

# def usdollar(money):
#     inr = money/usd
#     return inr

# def eudollar(money):
#     inr = money/euro
#     return inr

# Conversion = input("Enter a to convert in USD or b to convert in EURO:")

# if Conversion == "a":
#     a = usdollar(int(input("Enter Ammout in Rupees:")))
#     print(a)
# elif Conversion == "b":
#     b = eudollar(int(input("Enter Ammout in Rupees:")))
#     print(b)

#-------------------------------------------------

# Practice 8

# def armstrong(user_Input):
#     length = len(str(user_Input))
#     original = user_Input
#     b = 0
#     while user_Input > 0:
#         a = user_Input % 10
#         b = b + a**length
#         user_Input = user_Input // 10
#     if b == original:
#         print("Its a Armstrong number")
#     else:
#         print("It is not a Armstrong number")
#     return b

# c = armstrong((int(input("Enter the number to check whether its a armstrong number or not:"))))

#-------------------------------------------------

# Practice 9

# def print_Fibonacci(user_Input):
#     prepre = 0
#     pre = 1
#     current_value = 1

#     if user_Input < 0:
#         print("Invalid Input")
#         return

#     elif user_Input == 0:
#         print(prepre)
#         return prepre
#     elif user_Input == 1:
#         print(pre)
#         return pre
#     elif user_Input >=2:

#         for i in range(2, user_Input + 1):
#             current_value = pre + prepre
#             prepre = pre
#             pre = current_value

#         print(current_value)
#         return current_value

# b = print_Fibonacci(int(input("Enter number for fibonacci nummber:")))

#-------------------------------------------------

# Practice 10

# a = int(input("Enter first number to find LCM:"))
# b = int(input("Enter second number to find LCM:"))
# max_number = max(a, b)

# while True:
#     if(max_number%a == 0 and max_number%b == 0):
#         break
#     max_number = max_number + 1

# print(max_number)

#-------------------------------------------------

# Practice 11 HCF

# user_Input1 = int(input("Enter first number to find HCF:"))
# user_Input2 = int(input("Enter second number to find HCF:"))

# if user_Input1 > user_Input2:
#     a = user_Input2
#     b = user_Input1
# else:
#     a = user_Input1
#     b = user_Input2

# hcf = 1

# for i in range(2, a +1):
#     if a%i == 0 and b%i == 0:
#         hcf = i

# print(f"HCF is:{hcf}")

#-------------------------------------------------

# Prctice 12 Word finder

# import os
# contents = os.listdir()
# npython = 0
# def Found(filename):
#     with open(filename, 'r') as file:
#         filecon = file.read() 
#     if "python" in filecon.lower(): #finding word
#         return True
#     else:
#         return False


# for i in contents:
#     if i.endswith('py'):
#         print(f"Searching word in {i}:")
#         flag = Found(i)
#         if(flag):
#             print(f"python found in {i}")
#             npython = npython + 1
#         else:
#             print(f"python not found in {i}")

#-------------------------------------------------

# Practice 13 Add matrices

# def matrix():
#     m = int(input("Enter Value of m:"))
#     n = int(input("Enter Value of n:"))
#     matrix = []
#     for i in range(m):
#         row = []
#         for j in range(n):
#             num = int(input(f"Enter numbers in {i}{j}:"))
#             row.append(num)
#         matrix.append(row)
#     return matrix

# a = matrix()
# print(a)

#-------------------------------------------------

# prcatice 14 *
#             **
#             ***

# k = 1
# for i in range(0, 3):
#      for j in range(k):
#           print("*", end="")
#      k = k + 1
#      print()

#-------------------------------------------------

# practice 15 ***
#             **
#             *

# k = 3
# for i in range(3):
#     for j in range(k):
#         print("*", end = "")
#     k = k - 1
#     print()

#-------------------------------------------------

# practice 16 1 
#             1 2
#             1 2 3
#             1 2 3 4
#             1 2 3 4 5
#             1 2 3 4 5 6

# n = 7
# for i in range(n):
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print()

#-------------------------------------------------

# practice 17 6 5 4 3 2 1 
#             6 5 4 3 2 
#             6 5 4 3
#             6 5 4
#             6 5
#             6

# n = 6
# k = 6
# for i in range(n+1):
#     for j in range(k, i, -1):
#         print(j, end = " ")
#     print()

#-------------------------------------------------

# practice 18           * * 
#                     * * * * 
#                   * * * * * * 
#                 * * * * * * * * 
#               * * * * * * * * * * 

# for i in range(6):
#     for j in range(i, 6):
#         print(" ", end = " ")
#     for j in range(i):
#         print("*", end = " ")
#     for j in range(i):
#         print("*", end = " ")   
#     print()

#-------------------------------------------------

# practice 19








 


    








