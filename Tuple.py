# Declare a tuple variable
my_tuple = () # Blank tuple
print(my_tuple)
# Integer tuple
int_tuple = (2,60,40,-30,100)
print(int_tuple)

mixed_tuple = (1,"blue",33,"tt")
print(f"Mixed tuple :{mixed_tuple}")

# Nested tuple
nested_tuple = ("leaf" , 33, (2,3, (44,55,75)), "is nice")
print(nested_tuple[2][2][2])
print(nested_tuple[-2][-1][-3])




# Sets in python

my_set = {} #empty set
my_set = {11,22,2,3,5,8,4,34,34,1,1,2,3,3}
print(my_set)

# Updating sets
my_set.add(2)
my_set.add(5)

print(my_set)

# Set Union

set1 = {1,2,3,4,5}
set2 = {3,4,5,3,2}

print(set1.union(set2)) #combination of set2's unique elements
print(set1.intersection(set2)) #combination of set1 and set2 common element