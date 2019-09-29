convertTable = {
    "mile": 1609.0,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254,
    "km": 1000.0,
    "m": 1.0,
    "cm": 0.01,
    "mm": 0.001
}

s = input().split()
result = float(s[0]) * convertTable[s[1]]
if s[3] != "m":
    result = result / convertTable[s[3]]

print("{:.2e}".format(result))
