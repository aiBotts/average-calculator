total = 0
count = 0

def findAverage():
    global count
    global total
    display()
    value = float(input("Enter a number: "))
    if value != -1:
        float(input("Enter a number: "))
        total = total + value
        count = count + 1
    else:
        average = total / count
        print(value / average)
        return average

def display():
    print("This program calculates the average of")
    print("numbers entered by the user.")
    print("Press -1 to see your average.")

findAverage()