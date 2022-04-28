
def task_02():
    data = input("Enter digit: ")
    ev = 0
    nev = 0
    for x in data:
        if int(x) % 2 == 0:
            ev += 1
        else:
            nev += 1
    print(f"Even numbers: {ev} Not even numbers: {nev}")