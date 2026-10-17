# MAP() and Filter()
# Map applies to a function to each iteam in a list (or any iterable) and returns a map object (iterator)
# filter(function, iterable)
# filters elements of an iterable using a condition (returns only those that match True)
numbers = [1,2,3,4,5]
def sq(x):
    return x**2
def even(x):
    return x%2 == 0
sq_all_numbers = map(sq, numbers)
print(list(sq_all_numbers))
even_List = list(filter(even,numbers))
print(even_List)