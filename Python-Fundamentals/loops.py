# Level 1 – Basic loops
# Q1. Print numbers from 1 to 10 using a for loop.
# for i in range(1,11):
#     print(i)

# Q2. Print numbers from 10 to 1 using a for loop.
# for i in range(11,0,-1):
#     print(i)

# Q3. Print all even numbers from 1 to 50.
# for i in range(2,51,2):
#     print(i)

# Q4. Print all odd numbers from 1 to 50.
# for i in range(1,51,2):
#     print(i)

# Q5. Print the multiplication table of a number entered by the user.
# mul=int(input("enter a number:"))
# for i in range(1,11):
#     print(mul,"X",i,"=",mul*i)

# Q6. Calculate the sum of numbers from 1 to 100.
# total=0
# for i in range(1,101):
#     total=total+i
# print(total)

# Q7. Print numbers from 1 to 10 using a while loop.
# num=1
# while num<=10:
#     print(num)
#     num=num+1

# Q8. Print numbers from 10 to 1 using a while loop.
# num=10
# while num>=1:
#     print(num)
#     num=num-1

# Q9. Calculate the sum of even numbers from 1 to 50.
# total=0
# for i in range(2,51,2):
#     total=total+i
# print(total)

# Q10. Count how many numbers are divisible by 5 between 1 and 100.
# count=0
# for i in range(1,101):
#    if i%5==0:
#       count=count+1  
# print(count)

# Level 2 – Intermediate loops
# Q1. Find the factorial of a number.
# num=int(input("enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact=i*fact
# print(fact)

# Q2. Count the number of digits in an integer.
# count=0
# num=int(input("enter a number:"))
# while num>0:
#     num=num//10
#     count=count+1
# print(count)

# Q3. Calculate the sum of digits of a number.
total=0
num=int(input("enter a number"))
while num>0:
    num=num%10
    total=total+num
print(total)


    

