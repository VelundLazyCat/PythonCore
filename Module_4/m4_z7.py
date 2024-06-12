points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}
coordinates = [0, 1, 3, 2, 0]
f = 0


def calculate_distance(coordinates):
    distance = 0
    x = 0
    if len(coordinates) <= 1:
        return distance
    else:
        for i in range(len(coordinates)-1):
            if coordinates[x] < coordinates[x+1]:
                distance = distance + \
                    points.get((coordinates[x], coordinates[x+1]))
                x = x+1
            else:
                distance = distance + \
                    points.get((coordinates[x+1], coordinates[x]))
                x = x+1
        return distance


f = calculate_distance(coordinates)
print(f)
