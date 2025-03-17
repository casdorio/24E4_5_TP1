import time
import tracemalloc

def carregar_lista(arquivo_entrada):
    with open(arquivo_entrada, "r") as arquivo:
        return [linha.strip() for linha in arquivo]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

def medir_performance(ord_func, lista):
    lista_copia = lista[:]
    tracemalloc.start()
    inicio_tempo = time.time()
    ord_func(lista_copia)
    tempo_execucao = time.time() - inicio_tempo
    memoria_usada = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return tempo_execucao, memoria_usada

lista_original = carregar_lista("listagem.txt")

resultados = []
algoritmos = [
    ("Bubble Sort", bubble_sort, "O(n²)"),
    ("Selection Sort", selection_sort, "O(n²)"),
    ("Insertion Sort", insertion_sort, "O(n²) no pior caso, O(n) no melhor")
]

for nome, metodo, complexidade in algoritmos:
    tempo, memoria = medir_performance(metodo, lista_original)
    resultados.append((nome, tempo, memoria, complexidade))
    print(f"{nome}: {tempo:.6f} segundos, {memoria / 1024:.2f} KB, Complexidade: {complexidade}")

print("\nComparação Final:")
print("Algoritmo         | Tempo (s) | Memória (KB) | Complexidade")
print("-" * 55)
for nome, tempo, memoria, complexidade in resultados:
    print(f"{nome:<16} | {tempo:.6f} | {memoria / 1024:.2f} KB | {complexidade}")
