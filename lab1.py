def rotate(a, b, c):
    return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])


def jarvis_march(mas):
    n = len(mas)
    p = [i for i in range(n)]
    for i in range(1, n):
        if mas[p[i]][0] < mas[p[0]][0]:
            p[i], p[0] = p[0], p[i]
    h = [p[0]]
    del p[0]
    p.append(h[0])
    while True:
        right = 0
        for i in range(1, len(p)):
            if rotate(mas[h[-1]], mas[p[right]], mas[p[i]]) < 0:
                right = i
        if p[right] == h[0]:
            break
        else:
            h.append(p[right])
            del p[right]
    return h


mas = [[1, 2], [3, 4], [6, 2], [8, 7], [10, 7], [6, 9], [4, 3], [2, 8], [9, 8], [4, 6], [5, 7]]
print(jarvis_march(mas))
