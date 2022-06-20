n = int(input())

if (2 <= n <= 5):
    students = []
    
    for i in range(n):
        students.append([])
        students [i].append(str(input()))
        students [i].append(float(input()))

    #print(students)    

students.sort(key=lambda x: x[1])

#print(students)

min_marks = students[0][1]


students = [i for i in students if i[1]!=min_marks]

#print(students)    

min_marks = students[0][1]

students.sort(key = lambda x: x[0])
for i in students:
    if i[1] == min_marks:
        print(i[0])    
