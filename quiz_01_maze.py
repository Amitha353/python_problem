import numpy as np


def main_fun(grd, x, y):
    m, n = grd.shape
    var = np.zeros(grd.shape)
    lar = np.zeros(grd.shape)
    # go for the each point and check if its the shortes then calculate, replace with the shortest
    for a in range(m):
        for b in range(n):
            print(grd[a][b])
    print(grd[0][1])


maze = np.array([[0, 2, 0], [0, 0, 1], [1, 1, 1]])
x = 1
y = 1
main_fun(maze, x, y)
