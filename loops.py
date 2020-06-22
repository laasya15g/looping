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
