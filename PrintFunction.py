# print the numbers from 1....n as a string without spaces without using string method strip 
n = int(input())

if(1 <= n <= 150):
    for i in range(1,n+1):
        print(i, sep = '', end = '')