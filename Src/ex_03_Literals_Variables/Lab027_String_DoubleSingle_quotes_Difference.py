c= 'C'
c1 = "C"
print(c)
print(c1)
#dir= 'C:\sruti\n.txt' -> error as \s is not a valid escape sequence
# that's why double quotes are used in such cases along with 'r'
#'r' refers to raw that will ignore the escape sequence
dir= r"C:\sruti\n.txt"
print(dir)