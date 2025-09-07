class fast_greadient:

    def __init__(self, start_points, e):
        self.start_points = start_points
        self.e = e
    @staticmethod
    def f2(x1, x2):
        return 3 * x1 ** 2 - 3 * x1 * x2 + 4 * x2 ** 2 - 2 * x1 + x2

    def main(self):
        k = 0
        x = self.start_points
