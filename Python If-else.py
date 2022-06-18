# first solution for hacker rank
# sol. for Python If-else 

# take the input n
n = int(input().strip())

# 1<=n<=100
if (n>=1 and n<=100):

    if (n%2!=0 or (n%2==0 and n in range(6,21))):
        print("Weird")

    elif (n%2 == 0 and (n in range(2,6) or n>20)):
        print("Not Weird")



