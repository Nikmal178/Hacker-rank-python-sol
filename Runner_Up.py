n = int(input())
arr = list(map(int, input().split()))

# find the largest element
largest = max(arr)

# find the index of largest number and the number of occurences
# append the indexes to index_largest list and increase the count by 1
count = 0
index_largest = []
for i in range (len(arr)):
    if (arr[i] == largest):
        index_largest.append(i)
        count += 1

# check if largest value occurs more than once.
# if yes, then remove the elements of arr at index(elements of index_largest)
# The elements are removed in the reverse order as the index will be out of range for the arr list if 
# index_largest elements are traversed in original order.   
# For example: for arr = [2, 3, 5, 6, 6]
# The largest element is 6. 
# index_largest elements = [3, 4]
# intially index = 4, then arr.pop(4) = 6, arr = [2, 3, 5, 6], arr.length() = 4 with indexes 0, 1, 2, 3.
# Then index = 3, arr.pop(3) = 6, arr = [2, 3, 5]. 
 
if (count > 1 and count > 0):
    for index in index_largest[::-1]:
        arr.pop(index)    
    
elif (count == 1):
    arr.pop(index_largest[0])        
# after removing the largest elements find the maximum of arr and print the runner up.    
print(max(arr))    