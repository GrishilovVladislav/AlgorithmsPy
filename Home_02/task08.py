
def task_08():
    digits = input("Enter digits: ").split()
    x = int(input("Enter the number: "))
    result = 0
    for digit in digits:
        for number in digit:
            if int(number) == x:
                result += 1
    print(f"The number of your number: {result}")