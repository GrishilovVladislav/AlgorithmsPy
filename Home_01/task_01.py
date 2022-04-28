
class Task01():

    def get_sum_and_mul(self, digit):
        sum = 0
        mul = 1
        try:
            for d in str(digit):
                sum += int(d)
                mul *= int(d)
            return (sum, mul)
        except:
            raise ValueError("Bad input")
