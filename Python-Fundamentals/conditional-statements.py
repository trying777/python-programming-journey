# Q1. Take a number as input and check whether it is positive.
# num=int(input("enter a number:"))
# if num>0:
#     print("positive")

# Q2. Take a number and check whether it is positive, negative or zero.
# num=int(input("enter a number:"))
# if num>0:
#     print("positive")
# elif num==0:
#     print("zero")
# else:
#     print("negative")

# Q3. Take a number and check whether it is even or odd.
# num=int(input("enter a number:"))
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

# Q4. Take a person's age and check whether they are eligible to vote.
# age=int(input("enter a number:"))
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible")

# Q5. Take two numbers and print the greater number.
# num1=int(input("enter a number1:"))
# num2=int(input("enter a number2:"))
# if num1>num2:
#     print("the number 1 is greater",num1)
# else:
#     print("the number 2 is greater",num2)

# Q6. Take three numbers and find the largest number.
# num1=int(input("enter a 1st number:"))
# num2=int(input("enter a 2nd number:"))
# num3=int(input("enter a 3rd number:"))
# if num1>num2 and num1>num3:
#     print("1st number grester:",num1)
# elif num2>num1 and num2>num3:
#     print("2nd number greater:",num2)
# else:
#     print("3rd number greater:",num3)

# Q7. Take marks as input and display the grade: 90+ A, 75–89 B, 50–74 C, below 50 Fail.
# marks=int(input("enter a marks:"))
# if marks>=90:
#     print("A grade")
# elif marks>=75 and marks<=89:
#     print("B grade")
# elif marks>=50 and marks<74:
#     print("C grade")
# else:
#     print("fail")

# Q8. Take a year as input and check whether it is a leap year.
# year=int(input("enter a year:"))
# if year%400==0 or (year%4==0 and year%100!=0):
#     print("leap year")
# else:
#     print("not a leap year")

# year=2024
# print(year%400==0)
# print(year%4==0)
# print(year%100!=0)

# Q9. Take a character as input and check whether it is a vowel or consonant.
# char=input("enter any character:").lower()
# if char in ("a","e","i","o","u"):
#     print("vowel")
# else:
#     print("consonant")

# Q10. Take a number and check whether it is divisible by both 5 and 11.
# div=int(input("enter a number:"))
# if div%5==0 and div%11==0:
#     print("divisible by both 5 and 11")
# else:
#     print(" not divisible by both 5 and 11")

#Q11.Take age and check whether the person is eligible for a job (age between 18 and 35 inclusive).
# age=int(input("enter a age:"))
# if age>=18 and age<=35:
#     print("eligible for job")
# else:
#     print("not eligible for job")

# Q12. Take a username and password and check whether both match predefined values.
# name=input("enter your username:")
# password=(input("enter your password:"))
# if name=="varsha" and password=="Varsha@28":
#     print("login")
# else:
#     print("failed to login")

#Q13. Take a number and check whether it is a two-digit number.
# num=int(input("enter a numbers:"))
# if num>=10 and num<=99:
#     print("two digit number")
# elif num>=-99 and num<=-10:
#     print("two-digit number")
# else:
#     print("not a two-digit number")

#Q14.Take three sides of a triangle and check whether they can form a valid triangle.
# a=int(input("enter a 1 side of triangle:"))
# b=int(input("enter a 2 side of triangle:"))
# c=int(input("enter a 3 side of triangle:"))
# if a+b>c and a+c>b and b+c>a:
#     print("can form valid triangle")
# else:
#     print("cant form valid triangle")

# Q15. Create a simple calculator using if-elif-else that supports +, -, * and /.
print("simple calculator")
print("addition")
print("subtraction")
print("multiplition")
print("division")
operation=input("select a operation:").lower()
num1=float(input("enter a 1st number:"))
num2=float(input("enter a 2nd number:"))
if operation=="addition" or operation=="add":
    print(num1+num2)
elif operation=="subtraction" or operation=="sub":
    print(num1-num2)
elif operation== "multiplication" or operation=="mul":
    print(num1*num2)
elif operation== "division" or operation=="div":
    print(num1/num2)
else:
    print("invalid operation")






