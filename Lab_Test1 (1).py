#!/usr/bin/env python
# coding: utf-8

# In[7]:


def DecimalToBinary(num): 
      
    if num > 1: 
        DecimalToBinary(num // 2) 
    print(num % 2, end = '') 
  

if __name__ == '__main__': 
      
    InputNumber = input("Enter Number")
    dec_value = int(InputNumber)
      
   
    DecimalToBinary(dec_value) 


# In[9]:


FirstString = input("Enter Word ")
str = FirstString

Text_Size = 256
def getMaxOccuringChar(str): 
    
    count = [0] * Text_Size 
  
    
    max = -1
    c = '' 
  
    
    for i in str: 
        count[ord(i)]+=1; 
  
    for i in str: 
        if max < count[ord(i)]: 
            max = count[ord(i)] 
            c = i 
  
    return c

print ("Most occuring letter is " + getMaxOccuringChar(str))


# In[10]:


astring = "I have Python exam"

print(len(astring.split()))


# In[18]:


x = 10
a = 3
b = 4

def multiply_by_two(x):
    return x * 2

def add_numbers(a,b):
    return a + b


arguments = {
    x: 10,
    a: 3,
    b: 4
}

print (multiply_by_two(10))
print ("Arguments are: "+str(x))
print (add_numbers(3,4))
print ("Arguments are: "+str(a)+", "+str(b))


# In[20]:


a = 3
b = 4
def add_numbers(a,b):
   return a + b

def decoration_function(a, b):
   return (2*(3+4))

print(add_numbers(3, 4))
x = decoration_function(3,4)
print(decoration_function(a, b))
print("Arguments are: "+str(a)+", "+str(b))


# In[21]:


x = 10
def multiply_by_three(x):
    return x * 3


def augmented_multiply_by_three(x):
    return 2*(10 * 3)

arguments = {
    x : 10
    
}

print(multiply_by_three(10))
x = augmented_multiply_by_three(10)
print(augmented_multiply_by_three(x))
print ("Arguments are: "+str(x))


# In[ ]:




