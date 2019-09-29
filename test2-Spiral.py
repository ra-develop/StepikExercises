r = 0
while r <= 0:
    r = int(input())


array = []
w, h = r, r
array = [[None] * w for i in range(h)]


c = {'n': 1, 'x': 0, 'y': 0}


def change_element(n, index_x, index_y):
    if array[index_x][index_y] is None:
        array[index_x][index_y] = n
        return True
    else:
        return False


def f_rt():
    n = c['n']
    x = c['x']
    y = c['y']
    while y < r and change_element(n, x, y):
        y += 1
        n += 1
    c['n'] = n
    c['x'] = x+1
    c['y'] = y-1


def f_dn():
    n = c['n']
    x = c['x']
    y = c['y']
    while x < r and change_element(n, x, y):
        x += 1
        n += 1
    c['n'] = n
    c['x'] = x-1
    c['y'] = y-1


def f_lt():
    n = c['n']
    x = c['x']
    y = c['y']
    while y < r and change_element(n, x, y):
        y -= 1
        n += 1
    c['n'] = n
    c['x'] = x-1
    c['y'] = y+1


def f_up():
    n = c['n']
    x = c['x']
    y = c['y']
    while x < r and change_element(n, x, y):
        x -= 1
        n += 1
    c['n'] = n
    c['x'] = x+1
    c['y'] = y+1

if r != 1:
    while array[c['x']][c['y']] is None:
        f_rt()
        f_dn()
        f_lt()
        f_up()
    for i in range(r):
        for j in range(r):
            print(array[i][j], end=' ')
        print('')
else:
    print(r)
