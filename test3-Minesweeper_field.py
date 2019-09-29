# put your python code here
import re


def radar(f, x, y):
    if f[x][y] == '*':
        return '*'
    else:
        c = 0 + checklr(f, x, y)
        if x-1 >= 0:
            c += checklr(f, x-1, y)
        try:
            if f[x+1]:
                c += checklr(f, x+1, y)
        except IndexError:
            pass
        return str(c)


def checklr(f, x, y):
    c = 0
    if f[x][y] == '*':
        c += 1
    try:
        if f[x][y+1] == '*':
            c += 1
    except IndexError:
        pass
    if y-1 >= 0 and f[x][y-1] == '*':
        c += 1
    return c


while True:
    try:
        ranges = [int(i) for i in (input().split())]
    except ValueError:
        print('Range input error, repeat please')
        continue
    except AttributeError:
        print('Range input error, repeat please')
        continue
    if ranges and (1 <= ranges[0] <= 100) and (1 <= ranges[1] <= 100):
        break
    else:
        print('Range input error, repeat please')

p = re.compile('.')

field = [p.findall(input(), 0, ranges[1]) for i in range(ranges[0])]

for i in range(ranges[0]):
    output = ''
    for j in range(ranges[1]):
        output += field[i][j]
    print(output)
