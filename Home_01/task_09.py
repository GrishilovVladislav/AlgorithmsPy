
class Task09():
    def get_average(self, a, b, c):
        if b > a:
            a, b = b, a
        if c > a:
            a, c = c, a
        if b > c:
            return b
        else:
            return c