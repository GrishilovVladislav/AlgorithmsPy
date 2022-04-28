
def task_03():
    data = input("Enter digit: ")
    result = ""
    for i in range(len(data)):
        result += data[-(i+1)]
    print(f"New digit: {result}")