import string


class Task05():
    def get_position(self, x):
        x = x.lower()
        for i in range(len(string.ascii_lowercase)):
            if string.ascii_lowercase[i] == x:
                return i+1

    def get_amount(self, a, b):
        return abs(self.get_position(a) - self.get_position(b))