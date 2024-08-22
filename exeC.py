#leia um valor x e imprima q quantidade de linhas = x
x = int(input('Digite o número de linhas: '))

for i in range(x):
    for j in range(i + 1):
        print(j, end=' ')
    print()

