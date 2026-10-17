#Function that returns multiple values
def math_operation(num1,num2):
    return num1+num2,num1-num2,num1*num2,num1/num2
sum_r,diff_r,multi_r,div_r = math_operation(5,6)
print(sum_r,diff_r,multi_r,div_r)