palavras = list()

with open('loremipsum.txt', 'r') as file:
    for linha in file:
        palavras.extend(linha.split())

import time 

inicio = time.time()
palavras_bubble = palavras.copy()
for i in range(len(palavras_bubble)):
    for j in range(len(palavras_bubble) - 1):
        if palavras_bubble[j] > palavras_bubble[j + 1]:
            palavras_bubble[j], palavras_bubble[j + 1] = palavras_bubble[j + 1], palavras_bubble[j]

fim = time.time()
print("Tempo de execução do BUbble Sort:", fim - inicio)
print("Resultado do Bubble Sort:", palavras_bubble)

inicio = time.time()
palavras_selection = palavras.copy()
for i in range(len(palavras_selection)):
    min_idx = i
    for j in range(i + 1, len(palavras_selection)):    
        if palavras_selection[i] < palavras_selection[min_idx]:
            min_idx = j
    palavras_selection[i], palavras_selection[min_idx] = palavras_selection[min_idx], palavras_selection[i]
fim = time.time()
palavras_sort = palavras.copy()
palavras_sort.sort()
fim = time.time()
print("Tempo de execução do método sort:", fim - inicio) 
print("Resultado do método sort:", palavras_sort)   