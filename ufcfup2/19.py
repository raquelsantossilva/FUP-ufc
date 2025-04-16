def funcao(x):
    y1 = x//100
    resto = x % 100
    y2 = resto // 50
    resto = resto % 50
    y3 = resto // 20
    resto = resto % 20
    y4 = resto // 10
    resto = resto % 10
    y5 = resto // 5
    resto = resto % 5
    y6 = resto // 2
    resto = resto % 2
    y7 = resto // 1
    return y1, y2, y3, y4, y5, y6, y7
