
def funcao(x):
    y1 = x//3600
    ry1 = x % 3600
    y2 = ry1//60
    y3 = ry1 % 60
    return y1, y2, y3
