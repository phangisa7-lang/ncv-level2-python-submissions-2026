marks = []
i = 0
mark = int(input("Enter mark:  "))
count = 0
while mark != -1:
    marks.append(mark)
    i = i + 1
    
    mark = int(input("Enter mark: "))
    count += 1
sum = 0

for i in range(0,count):
    mark = marks[i]
    sum = sum + mark
    
    print((marks[i]))
print(f"The sum of all marks = {sum}")

## Get the average of all marks
total = 0
for i in range(len(marks)):
    mark = marks[i]
    total = total + mark

avg = total / len(marks)
print(f"The average of all marks = {avg}")