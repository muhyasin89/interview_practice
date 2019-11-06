import math
from itertools import combinations


def dist(p1,p2):
    (x1, y1), (x2, y2) = p1, p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

x1 = input("input nilai x1:")
x2 = input("input nilai x2:")
x3 = input("input nilai x3:")

y1 = input("input nilai y1:")
y2 = input("input nilai y2:")
y3 = input("input nilai y3:")

x=[int(x1),int(x2),int(x3)]
y=[int(y1),int(y2),int(y3)]


points = list(zip(x,y))

distances = [dist(p1, p2) for p1, p2 in combinations(points, 2)]
avg_distance = sum(distances) / len(distances)

print("average {}".format(avg_distance))