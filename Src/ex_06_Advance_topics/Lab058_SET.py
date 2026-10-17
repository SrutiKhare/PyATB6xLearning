# SET is an unordered collection of data type that is iterable, mutable and has no duplicate elements
# it does not allow duplicates and is mainly used for membership testing, removing duplicates, and
# mathematical set operations
# Set operations (Mathematical)
# Union(| or union)
# Intersection (& or intersection)
# Difference (- or difference)
#symmetric difference : element in either set but not both (^)
a={1,2,3}
b={3,4,5,6}
print(a.union(b))
print(a | b )
print(a & b )
print(a.intersection(b))
print(a-b)
print(b.difference(a))
print(a^b)