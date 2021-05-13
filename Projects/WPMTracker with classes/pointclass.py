import matplotlib.pyplot as plt

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x,y)
        else:
            x = self.x + other
            y = self.y + other
            return Point(x,y)

    def plot(self):
        plt.scatter(self.x, self.y)
        plt.show()


a = Point(0,2)
d = a + Point(1,1)

print(d.x,d.y)