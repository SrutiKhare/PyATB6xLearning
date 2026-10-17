
squares = {x ** 2 for x in range(5)}
print(squares)
square2 = set()
for x in range(5):
    #square2[x] = x**2
    square2.add(x**2)

print("\n\n")
print(square2)