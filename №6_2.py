class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asphalt_weight(self, weigh, thickness):
        return self._length * self._width * weigh * thickness / 1000


my_road = Road(5000, 20)
print(my_road.asphalt_weight(25, 5))