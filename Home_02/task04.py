
def task_04():
    n = int(input("Enter n: "))
    s = 0
    for i in range(n):
        s += ((-1)**(i))/(2**(i))
    print(f"Sum: {s}")