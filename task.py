# Create an empty list called my_lits
my_list = []
print(my_list)

# Append the following elements to my_list: 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print('After append:', my_list)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)
print('After insert:', my_list)

# Extend my_list with another list: [50, 60, 70]
list_2 = [50, 60, 70]
my_list.extend(list_2)
print('After extending:', my_list)

# Remove the last element from my_list
my_list.remove(70)
print('After remove:',my_list)

# Sort my_list in ascending order.
my_list.sort
print('After sorting:',my_list)

# Find and print the index of the value 30 in my_list.
index_30 = my_list.index(30)
print('Index of 30:', index_30)
