# i/p - r -float
# 0/p - string formatted output of area
# Logic Bulding Formula
"""
Logic Building Formula
// Step 1 //
Figure out the inputs and output
input -> r -> data type -> float
pi = 3.14
power -> pow or ** -> any
o/p -> String -> float - area, print area

// Step 2 //
rough logic = area = 3.14 * pow(r,2)

// Step 3 //
"""
radius = float(input("Enter radius: "))
print(radius)
#area = 3.14
area = 3.14 * (pow(radius,2))
print("Area of the circle is -> ",area)
