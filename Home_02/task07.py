
def task_07():
    n = int(input("Enter n for check: "))
    s_1 = 0
    s_2 = 0
    for i in range(n):
        s_1 += (i+1)
    s_2 = n*(n+1)/2
    print(f"Sum of n-elements with cycle: {s_1}\n"
          f"Sum of n-elements with formula: {s_2}")