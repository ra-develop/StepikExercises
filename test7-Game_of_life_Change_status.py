

w = int(input("Enter wide : "))
h = int(input("Enter height : "))

print("Please enter Field of Life. Empty cell is '.'. Cell with live is 'X'.")
field = []

for i in range(h):
    field.append(list(input().ljust(w,'.')[0:w]))

print(field)

