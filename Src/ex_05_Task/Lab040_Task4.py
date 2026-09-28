# Find the max num:
num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))
num3=int(input("Enter another number:"))
if num1>=num2 and num1>=num3:
    max=num1
elif num1>=num2 and num1<=num3:
    max=num3
else:
    max=num2
print(max)
