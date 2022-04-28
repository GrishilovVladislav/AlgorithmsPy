
def task_09():
    digits = input("Enter digits: ").split()
    max_n = 0
    temp_n = 0
    max_digit = ""
    for digit in digits:
        for number in digit:
            temp_n += int(number)
        if temp_n > max_n:
            max_n = temp_n
            max_digit = digit
        temp_n = 0
    print(f"Maximum number-sum in {max_digit}: {max_n}")