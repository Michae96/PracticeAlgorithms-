from collections import namedtuple
from itertools import combinations
from math import sqrt

Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2

def closest_pair(X, Y): 
    if len(X) == 2:
        return distance_squared(X[0], X[1])
    if len(X) == 3:
        return min(distance_squared(X[0], X[1]), distance_squared(X[0], X[2]), distance_squared(X[1], X[2]))
    mid = len(X) // 2 if len(X) % 2 == 0 else (len(X) // 2) + 1
    
    d1 = closest_pair(X[:mid], Y[:mid])
    d2 = closest_pair(X[mid:], Y[mid:])
    d = min(d1, d2)
    S = [point for point in Y if ((point.x <= X[mid].x + d) and (point.x >= X[mid].x - d))]
    for i in range(len(S)):
        for j in range(1, 8):
            if i + j < len(S):
                d = min(d, distance_squared(S[i], S[i+j]))

    return d

def minimum_distance_squared(points):
    X = sorted(points, key=lambda point: point.x)
    Y = sorted(points, key=lambda point: point.y)
    return closest_pair(X, Y)

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))