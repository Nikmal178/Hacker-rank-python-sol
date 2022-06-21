from turtle import pen


n = int(input())
dict = {}

for i in range(n):
        marks = []    
        name_marks = list(map(str, (input().split())))
        for elements in name_marks:
            ele_index = name_marks.index(elements)
            if ele_index == 0:
                name = name_marks[ele_index]
            else:
                marks.append(float(name_marks[ele_index]))     
        dict[name] = marks
              
average = 0
sum = 0
total = 0
student = str(input())
for key in dict.keys():
   if student == key:
    for value in dict.get(key):
        sum += value
        total += 1
         
     
    average = float(sum/total)
    print("{:.2f}".format(average))        

        

    