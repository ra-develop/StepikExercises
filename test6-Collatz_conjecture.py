# put your python code here
def collatz(m):
    if m % 2 == 0:
        return(m/2)
    else:
        return(m*3+1)

n = int(input())

while True:
    if n == 1:
        break
    print(int(n), end=' ')
    n = collatz(n)

print(int(n))
