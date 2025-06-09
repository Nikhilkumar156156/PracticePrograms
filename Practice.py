#1 First

# def calculator(first=int(input("enter a number")),second=int(input("enter sec number"))):
#     c=(input("Enter a for Addition, s for Substraction, d for Divide, m for Multiplication"))
#     if (c=="a"):
#       e=first+second
#       print(e)
#     elif (c=="s"):
#       e=first-second
#       print(e)
#     elif (c=="d"):
#       e=first/second
#       print(e)
#     elif (c=="m"):
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

usd = 85.79
inr = 1
euro = 97.81

def usdollar(money):
    inr = money/usd
    return inr

def eudollar(money):
    inr = money/euro
    return inr

Conversion = input("Enter a to convert in USD or b to convert in EURO:")

if Conversion == "a":
    a = usdollar(int(input("Enter Ammout in Rupees:")))
    print(a)
elif Conversion == "b":
    b = eudollar(int(input("Enter Ammout in Rupees:")))
    print(b)


    








