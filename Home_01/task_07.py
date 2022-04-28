
class Task07():
    def is_exists(self, a, b, c):
        if b > a:
            a, b = b, a
        if c > a:
            a, c = c, a
        if a >= b + c:
            return False
        else:
            return True

    def get_type(self, a, b, c):
        if a == b == c:
            return "Equilateral"
        if a == b or a == c or b == c:
            return "Isosceles"
        else:
            return "Versatile"
