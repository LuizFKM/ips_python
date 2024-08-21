import random
n = 8
vetorA = [0] * n
vetorB = [0] * n

for i in range(n):
   vetorA[i] = random.randint(1,100)
   vetorB[i] = vetorA[i] * 2
