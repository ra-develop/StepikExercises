import re

base = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
    4: 'IV',
    9: 'IX',
    40: 'XL',
    90: 'XC',
    400: 'CD',
    900: 'CM'
}

while True:
    year = input()
    try:
        if year and (0 < int(year) < 4000):
            break
        else:
            print('Range input error, repeat please')
    except ValueError:
        print('Range input error, repeat please')
        continue
    except AttributeError:
        print('Range input error, repeat please')
        continue


p = re.compile('.')

field = p.findall(year.zfill(4), 0)

print(field)

result = ''
for c in range(4):
    s = 0
    # thousands
    i = field[c]
    if i != '0' and c == 0:
        for j in range(int(i)):
            result += base[1000]
        continue
    # hundreds
    if i != '0' and c == 1:
        if i == '4':
            result += base[400]
            continue
        elif i == '9':
            result += base[900]
            continue
        if 5 <= int(i) <= 8:
            s = 5
            result += base[500]
        if i == '5':
            continue
        for j in range(s, int(i)):
            result += base[100]
        continue
    # decimals
    if i != '0' and c == 2:
        if i == '4':
            result += base[40]
            continue
        elif i == '9':
            result += base[90]
            continue
        if 5 <= int(i) <= 8:
            s = 5
            result += base[50]
        if i == '5':
            continue
        for j in range(s, int(i)):
            result += base[10]
        continue
    # units
    if i != '0' and c == 3:
        if i == '4':
            result += base[4]
            continue
        elif i == '9':
            result += base[9]
            continue
        if 5 <= int(i) <= 8:
            s = 5
            result += base[5]
        if i == '5':
            continue
        for j in range(s, int(i)):
            result += base[1]
        continue

print(result)
