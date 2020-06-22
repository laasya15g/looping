#!/usr/bin/env python
# coding: utf-8

# In[16]:


terms=int(input("enter the number of terms:"))
i=0
j=1 #initialsing the first 2 numbers
count=0;

if terms<=0 :
    print("print the valid postive number")
    terms=int(input("enter the number of terms:"))
elif terms == 1 :
    print("fibancci series:1")
else:
    pass

print("fibanacci sequence for given no of terms","%i"%terms)
while count<=terms :
    k=i+j
    print(i)
    i=j
    j=k
    count+=1


# In[34]:


list1=[14,34,-87,98,-43,21,-65]
print(list1)
for iterate in list1:
    if iterate > 0:
        print(iterate,",",end=" ")
print( )

list2=[12,14,-54,89,67,-34]
print(list2)
new_list = list(filter(lambda n: n>0 ,list2)) #we can use lamba for single iteration than looping for functions and filter
                                              #and check the iteratable for the given list with the help of function 
print(new_list)


# In[ ]:




