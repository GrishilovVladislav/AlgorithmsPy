import random


def task_06():
    answer = random.randint(0,100)
    i = 1
    while (x := int(input("Enter digit: "))) != answer and i != 10:
        if answer > x:
            print(f"The answer is bigger than {x}")
        else:
            print(f"The answer is lower than {x}")
        print(f"Tries remain: {10-i}")
        i += 1
    print (f"The answer is {answer}")