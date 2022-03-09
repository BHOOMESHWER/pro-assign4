#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Write a Python Program to Find the Factorial of a Number');get_ipython().run_line_magic('pinfo', 'Number')
get_ipython().set_next_input('2. Write a Python Program to Display the multiplication Table');get_ipython().run_line_magic('pinfo', 'Table')
get_ipython().set_next_input('3. Write a Python Program to Print the Fibonacci sequence');get_ipython().run_line_magic('pinfo', 'sequence')
get_ipython().set_next_input('4. Write a Python Program to Check Armstrong Number');get_ipython().run_line_magic('pinfo', 'Number')
get_ipython().set_next_input('5. Write a Python Program to Find Armstrong Number in an Interval');get_ipython().run_line_magic('pinfo', 'Interval')
get_ipython().set_next_input('6. Write a Python Program to Find the Sum of Natural Numbers');get_ipython().run_line_magic('pinfo', 'Numbers')


# 1. Write a Python Program to Find the Factorial of a Number?

# In[12]:


num = int(input("Enter a number: "))  
factorial = 1  
if num < 0:  
    print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
    print("The factorial of 0 is 1")  
else:  
    for i in range(1,num + 1):  
        factorial = factorial*i  
print("The factorial of",num,"is",factorial)


# 2. Write a Python Program to Display the multiplication Table?

# In[14]:


num = int(input("Show the multiplication table of? "))  
# using for loop to iterate multiplication 10 times   
for i in range(1,11):  
    print(num,'x',i,'=',num*i)  


# 3. Write a Python Program to Print the Fibonacci sequence?

# In[ ]:


nterms = int(input("How many terms you want? "))  
# first two terms  
n1 = 0  
n2 = 1  
count = 2  
# check if the number of terms is valid  
if nterms <= 0:  
    print("Plese enter a positive integer")  
elif nterms == 1:  
    print("Fibonacci sequence:")  
    print(n1)  
else:  
    print("Fibonacci sequence:")  
    print(n1,",",n2,end=', ')  
    while count < nterms:  
        nth = n1 + n2  
        print(nth,end=' , ')  
# update values  
n1 = n2  
n2 = nth  
count += 1  


# 4. Write a Python Program to Check Armstrong Number?

# In[19]:


# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# display the result
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")


# 5. Write a Python Program to Find Armstrong Number in an Interval?

# In[14]:


lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
for num in range(lower,upper + 1):  
    sum = 0  
    temp = num  
    while temp > 0:  
        digit = temp % 10  
        sum += digit ** 3  
        temp //= 10  
        if num == sum:  
            print(num)  


# 6. Write a Python Program to Find the Sum of Natural Numbers?

# In[18]:


num = int(input("Enter a number: "))  
if num < 0:  
    print("Enter a positive number")  
else:  
    sum = 0  
# use while loop to iterate un till zero
while(num > 0):  
    sum += num  
    num -= 1  
    print("The sum is",sum)  


# In[ ]:




