"Name: Alex Perez Perez"
"Date: 06/17/2026"
"Description: This Program that has some practice with arrays and create inserting and searching for items"
"inside the arrry"

#Array of characters
my_array = ['E', 'N', 'G', 'R', '2', '2', '1']

my_array.insert(7, 'X') #Variable to insert an item into the array

#loop to print the items in the array
for item in my_array:
    print(item)

target = 'R' 

# Loop to search for the target item in the array
for item in my_array:
    if item == target:
        print("found {} in the array".format(target))
    else:
        print("not found {} in the array".format(target))

item == target 

selectionSort(A):
for each index i in length(A):
let min_idx ß i
for each index j from i+1 to length(A):
if A[j] < A[min_idx]:
min_idx ß j
swap A[i] and A[min_idx]