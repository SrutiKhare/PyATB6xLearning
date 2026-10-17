# Write a sum function to add three no.s
def sum_3numbers(num1=1,num2=2,num3=3):
    return num1+num2+num3
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
print("Sum of the given no.s is :",sum_3numbers(n1,n2,n3))
result1=sum_3numbers(30,40,60)
result2= sum_3numbers()
result3= sum_3numbers(num1=40)
result4= sum_3numbers(num1=30,num2=20)
result5=sum_3numbers(num1=30,num2=20,num3=66)
print(result1,result2,result3,result4,result5)
# Argument Name should not be same as input variable name