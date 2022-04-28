import random
import string


class Task04():
    def get_random_int(self, a, b):
        return random.randint(a, b)

    def get_random_float(self, a, b):
        return random.uniform(a, b)

    def get_random_char(self, a, b):
        return random.choice(string.ascii_letters.split(a)[1].split(b)[0])
