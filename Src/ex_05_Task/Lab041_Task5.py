# Grade calculator :
"""
Write a program that calculates and displays the letter grade
fpr a given numerical score
based on following grading scale :
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
"""
score=int(input("Enter your score: "))
if score<0 or score>100:
    print("You are a superman!!!!")
else:
    if score>=90:
        print("A")
    elif score>=80:
        print("B")
    elif score>=70:
        print("C")
    elif score>=60:
        print("D")
    else:
        print("F")