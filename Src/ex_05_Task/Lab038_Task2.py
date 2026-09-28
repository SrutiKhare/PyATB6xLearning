"""Write a program to take a user age and decide whether he can go to club or not"""
age = int(input("Enter your age:"))
if age >0 and age <100:
        if age <21:
            print("You can't go to club")
        else:
            print("You are old enough to go to club")
else:
    print("Enter a valid age")
