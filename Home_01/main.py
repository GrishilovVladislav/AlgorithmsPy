import task_01, task_02, task_03, task_04, task_05, task_06, task_07, task_08, task_09

class WorkWithData():
    @staticmethod
    def print_answer(data, i = 0):
        print("="*100, end="\n\n")
        print(f"Answer('s) in task_0{i}: ", end="")
        for x in data:
            print (f" {x} ", end="")
        print("\n\n" + "="*100, end="\n")


if __name__ == '__main__':

###########################__TASK_01__###########################

    print("Enter digit: ", end="")
    WorkWithData.print_answer(task_01.Task01().get_sum_and_mul(int(input())), 1)

###########################__TASK_02__###########################

    list = [task_02.Task02().bit_translation_and(5, 6)]
    list.append(task_02.Task02().bit_translation_or(5, 6))
    list.append(task_02.Task02().bit_translation_left(5, 2))
    list.append(task_02.Task02().bit_translation_right(5, 2))
    WorkWithData.print_answer(list, 2)

###########################__TASK_03__###########################

    print("Enter coordinates of the first dot in x,y - format: ", end="")
    data = input()
    dot_01 = (int(data.split(",")[0]), int(data.split(",")[1]))
    print("Enter coordinates of the first dot in x,y-format: ", end="")
    data = input()
    dot_02 = (int(data.split(",")[0]), int(data.split(",")[1]))
    WorkWithData.print_answer(task_03.Task03().get_equation(dot_01, dot_02), 3)

###########################__TASK_04__###########################

    print("Enter int borders in {start}:{end} - format: ", end="")
    data = input()
    boarders = [(int(data.split(":")[0]), int(data.split(":")[1]))]
    print("Enter int float in {start}:{end} - format: ", end="")
    data = input()
    boarders.append((float(data.split(":")[0]), float(data.split(":")[1])))
    print("Enter int char in {start}:{end} - format: ", end="")
    data = input()
    boarders.append((data.split(":")[0], data.split(":")[1]))
    WorkWithData.print_answer((task_04.Task04().get_random_int(boarders[0][0], boarders[0][1]),
                               task_04.Task04().get_random_float(boarders[1][0], boarders[1][1]),
                               task_04.Task04().get_random_char(boarders[2][0], boarders[2][1])), 4)

###########################__TASK_05__###########################

    print("Enter letters in {letter_1} {letter_2} - format: ", end="")
    data = input()
    letters = (data.split()[0], data.split()[1])
    WorkWithData.print_answer((task_05.Task05().get_position(letters[0]),
                               task_05.Task05().get_position(letters[1]),
                               task_05.Task05().get_amount(letters[0], letters[1])), 5)

###########################__TASK_06__###########################

    print("Enter number: ", end="")
    WorkWithData.print_answer(task_06.Task06().get_letter(int(input())), 6)

###########################__TASK_07__###########################

    print("Enter lengths: ", end="")
    lengths = input().split()
    WorkWithData.print_answer((task_07.Task07().is_exists(int(lengths[0]), int(lengths[1]), int(lengths[2])),
                               task_07.Task07().get_type(int(lengths[0]), int(lengths[1]), int(lengths[2]))), 7)

###########################__TASK_08__###########################

    print("Enter year: ", end="")
    WorkWithData.print_answer([task_08.Task08().is_leap_year(int(input()))], 8)

###########################__TASK_09__###########################

    print("Enter digits: ", end="")
    digits = input().split()
    WorkWithData.print_answer([task_09.Task09().get_average(int(digits[0]), int(digits[1]), int(digits[2]))], 9)