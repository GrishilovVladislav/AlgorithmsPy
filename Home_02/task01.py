
def task_01():
    data = input("Enter data a{+-/*}b: ")
    b = ""
    for x in data:
        if x == '+' or x == '-' or x == '*' or x == '/':
            a = b
            s = x
            b = ""
            continue
        b += x
    operations = {"+": int(a) + int(b),
                  "-": int(a) - int(b),
                  "*": int(a) * int(b),
                  "/": int(a) / int(b)
    }
    print(f"Answer: {operations[s]}")