# print even numbers :
num =int(input("Enter a number:"))
print("Even no.s are :")
for i in range(1,num+1):
    if(i%2==0):
        print(i)
print("Odd no.s are :")
for i in range(1,num+1):
    if(i%2!=0):
        print(i)
