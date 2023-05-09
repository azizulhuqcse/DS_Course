# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:37:30 2023

@author: asumo
"""
import pandas as pd


# 1. Take values of the length & breadth of a rectangle from user input and check if it is square or not.
Length=float(input("Enter the length of the rectangle :"))
Breadth=float(input("Enter the breadth of the rectangle :"))
#Checking the rectangle is Square or Not.

if Length==Breadth:
    print("The rectangle is a Square")
else:
   print("The rectangle is not a Square")

#2. Take three integer values from the user and print the greatest among them.

Number1=int(input("Enter the 1st Number :"))
Number2=int(input("Enter the 2nd Number :"))
Number3=int(input("Enter the 3rd Number :"))

if Number1>Number2 and Number1>Number3:
    print("The greates number is:",Number1)
    
elif Number2>Number1 and Number2>Number3:
    print("The greates number is:",Number2)
    
else:
    print("The greates number is:",Number3)

#Using Max Function
Max_Number=max(Number1,Number2,Number3)
print("The higher number is :",Max_Number)

#3. A student will not be allowed to sit in an exam if his/her attendance is less than 75%.

Total_class=int(input("Total number of the class:"))
Student_Attendence=int(input("Total attendence of the class:"))
Attendence_Percentage=(Student_Attendence / Total_class)*100
print("Student percentage to attend the class : ",Attendence_Percentage)
if Attendence_Percentage <75:
    print("Student is not allowed to sit on the exam")
else:
    print("Student is allowed to sit the exam")


#4. A school has the following rules for the grading system:
#Below 25 – F, 25 to 44 – E, 45 to 49 – D, 50 to 59 – C, 60 to 79 – B, 80 to 89 - A, Above 90 - A+
#Now, Ask the user to enter marks and print the corresponding grade.

Student_Marks=int(input("Please enter the subject marks :"))

if Student_Marks <25:
    grade="F"
elif Student_Marks<45:
    grade="E"
elif Student_Marks<50:
    grade="D"
elif Student_Marks<60:
    grade="C"
elif Student_Marks<80:
    grade="B"
elif Student_Marks<90:
    grade="A"
else:
    grade="A+"
print("The student marks is (",Student_Marks,") and Grade is",grade)

#5. Print the following pattern using for and while loop.
#Outer loop control the number of rows
for i in range(7,3,-1): 
#Inner loop prints the number of each row    
    for j in range(1,i+1): 
        print(j,end=' ')
    print()
   
i=7
while i>3:
    j=1
    while j<=i:
        print(j,end=' ')
        j+= 1
    print()
    i-= 1
   
# 6 Display numbers from -100 to -10 using for loop.

for i in range(-100,-9):
    print(i)

#7. Write a program to sum all prime numbers within a range of 10 to 1000.
num1=int(input("Please enter the starting number :"))
num2=int(input("Please enter the Ending number :"))
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

Sum_of_primes=0
for i in range(num1,num2):
    if is_prime(i):
        Sum_of_primes +=i
print("The sum of the prime number between ",num1," and ",num2," is:",Sum_of_primes)


#8. Find the factorial of an n! (Hint, n=7: 7*6*5*4*3*2*1)

n=int(input("Please enter the Number:"))
def factorial(n):
    factorial =1
    for i in range(n):
        factorial*=i+1
    return factorial
print("The Factorial of ",n," is :",factorial(n))

#9. Reverse a given integer number 27956240710.

number=27956240710
number=str(number)
reverse_number=number[::-1]
print("The reverse number of ",number,"is:",reverse_number)

#10. Print the following pattern using for and while loop.
  
for i in range(3,5):
    if i <=5:
        print("# " *i)
    elif i<5:
        print("#" *(5-i))
    else:
        print("#" *(4-i))
 
#11. Display the Fibonacci series of 15 elements using the for and while loop.
n=int(input("Enter the number :"))
def fibonacci(n):
    sequence=[0,1]
    while sequence[-1]<n:
        sequence.append(sequence[-1]+sequence[-2])
    return sequence[:-1]
#n=input("Enter a number :")
#n=int(n)
print(fibonacci(n))

#Python Inbuilt Data Stracture
Li=[1,3,5,[2,3],True]

#print(Li)
Li[3].remove(2)
Li[3].append(3)
Li[-1]=False
print(Li)

#Find the intersection (common) of two sets.
S1 ={1,4,6,8}
S2 ={True,1,2,10}
result=S1&S2
print(result)

#14. Input a list from the user then Remove duplicates from a list and create a set and find the max
#number. User_input = [1,9,3,4,5,200,54]
given_number=[1,9,3,4,5,200,54]
user_input = input("Enter a list of numbers seperated by commas: ")
list_number=user_input.split(",")  
list_number=[int(i) for i in list_number]
print(list_number)
remove_duplicate=set( given_number + list_number)
print(remove_duplicate)
max_number=max(remove_duplicate)
print(max_number)


#15. Rename the key of a dictionary.
#Write a program to rename a key ‘country’ to a ‘region’ in the following dictionary.

Dict = { "name": "Shakil", "age":27, "city": "Berlin", "country": "Germany" }
print(Dict)
Dict['region']=Dict.pop('country')
print(Dict)


#16 Creating a data frame using the list.
# num = [10,100,300] (column name is number)

num = [10,100,300]
data={"number":num}
df=pd.DataFrame(data)
print(df)

#17. Change the value of a key in a given dictionary.
#Write a Python program to change ‘age’ to 28 in the following dictionary.

Dict = { "name": "Shakil", "age":27, "city": "Berlin", "country": "Germany"}
Dict["age"]=28
print(Dict)








