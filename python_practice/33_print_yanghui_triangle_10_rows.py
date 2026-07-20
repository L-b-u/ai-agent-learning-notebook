yh = []
for i in range(10):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = yh[i-1][j-1] + yh[i-1][j]
    yh.append(row)


max_width = len(' '.join(map(str, yh[-1])))
for row in yh:
    print(' '.join(map(str, row)).center(max_width))