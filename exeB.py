n = 3
for i in range(n):
    for j in range(1, i+2):
        print(j, end=' ')
    print()
for i in range(n-1):
    for j in range(1,n-i, 1):
        print(j, end=' ')
    print()
