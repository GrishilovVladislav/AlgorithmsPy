
def task_05():
    k = 1
    for i in range(32,128):
        print(f"  {i} : {chr(i)}", "|", sep="\t", end="")
        k += 1
        if k == 10:
            k = 1
            print("\n", "-"*107)
    print("\n")