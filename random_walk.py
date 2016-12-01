from random import choice

class RandomWalk():
    """class to generate  random walks."""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        #All walks start from (0, 0)
        self.x_value = [0]
        self.y_value = [0]
