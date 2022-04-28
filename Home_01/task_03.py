
class Task03():
    def get_equation(self, dot_1, dot_2):
        x_1 = int(dot_1[0])
        y_1 = int(dot_1[1])
        x_2 = int(dot_2[0])
        y_2 = int(dot_2[1])
        k = (y_1 - y_2) / (x_1 - x_2)
        b = y_1 - k * x_1
        return [f"y = {k}x + {b}"]