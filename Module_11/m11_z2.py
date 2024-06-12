class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        if x >= 0:
            self.__x = x
        else:
            print('Only numbers greater zero accepted')

    @y.setter
    def y(self, y):
        if y >= 0:
            self.__y = y
        else:
            print('Only numbers greater zero accepted')


point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10
