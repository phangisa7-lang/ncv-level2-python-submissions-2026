def getMark():
    marks = []
    while True:
        mark = int(input("Enter mark (-1 to stop): "))
        if mark == -1:
            break
        marks.append(mark)
    return marks

def print_list_size(marks):
    print(f"Our list has {len(marks)} elements")

def print_marks_size(marks):
    for x in range(len(marks)):
        print(f"Mark {x+1} is {marks[x]}")
        
def get_sum_of_marks(marks):
    total = 0
    for x in range(len(marks)):
        total = total + marks[x]
    return total  

def determine_highest(marks):
    if len(marks) == 0:
        print("No marks entered yet - Press 1 first")
        return
    
    highest = marks[0]
    for i in range(len(marks)):
        current_mark = marks[i]  
        if current_mark > highest:
            highest = current_mark
    print(f"The highest mark is {highest}")  


menu = 'Press 1: Capturing marks\n'
menu += 'Press 2: Check number of marks\n'
menu += 'Press 3: To calculate sum of marks\n'
menu += 'Press 4: To find the highest mark\n'
menu += 'Press -1: To exit\n'

entered_marks = []

while True:
    print(menu)
    choice = int(input(': Make a choice: '))

    if choice == 1:
        entered_marks = getMark()
        print_marks_size(entered_marks)

    elif choice == 2:
        print_list_size(entered_marks)
        
    elif choice == 3:
        calc_sum = get_sum_of_marks(entered_marks)
        print('Sum of all marks = ', calc_sum)

    elif choice == 4:
        determine_highest(entered_marks)

    elif choice == -1 or choice == 5:
        print('Thank you for using the App')
        break
        
    else:
        print('Not on the menu')