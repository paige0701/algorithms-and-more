import random


class MSDie:
    """ (This is a docstring)
    Multi-sided die

    Instance Variables:
        current_value
        num_sides
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randint(1, self.num_sides)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return f"MSDie({self.num_sides}) : {self.current_value}"

    def __eq__(self, other):
        return self.current_value == other.current_value

    def __lt__(self, other):
        return self.current_value < other.current_value

    def __le__(self, other):
        return self.current_value <= other.current_value


if __name__ == '__main__':

    my_die = MSDie(6)
    for i in range(5):
        print(my_die)
        my_die.roll()

    d_list = [MSDie(6), MSDie(20)]
    print(d_list)

    x = MSDie(6)
    y = MSDie(7)

    x.current_value = 6
    y.current_value = 5

    print(x == y)
    print(x < y)
    print(x > y)
    print(x != y)
    print(x <= y)
    print(x >= y)
    print(x is y)