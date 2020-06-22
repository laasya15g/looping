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
