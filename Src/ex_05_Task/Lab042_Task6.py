# Write a factorial program :
num=int(input("Enter a number: "))
if num<0:
    print("Invalid Input")
else:
    factorial = 1
    for i in range(1, num + 1):
        #factorial = i * (i - 1)
        factorial = factorial * i
    print(factorial)