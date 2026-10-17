# write a program that prints number from 1 to 50 and prints fizz for multiples of 3, buzz for multiples of 5 and fizzbuzz for multiple of both
for i in range(1,51):
    if(i%3==0) and (i%5==0):
        print("FrizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)