import task01, task02, task03, task04, task05, task06, task07, task08, task09

if __name__ == '__main__':
    tasks ={1: task01.task_01,
            2: task02.task_02,
            3: task03.task_03,
            4: task04.task_04,
            5: task05.task_05,
            6: task06.task_06,
            7: task07.task_07,
            8: task08.task_08,
            9: task09.task_09

            }
    print("=" * 100)
    try:
        while True:
            tasks[int(input("Enter the task number: "))]()
            print("=" * 100)
    except:
        print("Bad input!")
