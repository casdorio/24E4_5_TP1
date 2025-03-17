import time
import tracemalloc
from collections import deque

def carregar_arquivo(caminho):
    with open(caminho, 'r') as f:
        return [linha.strip() for linha in f.readlines()]

def medir_performance(func, *args):
    tracemalloc.start()
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    memoria_usada = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return resultado, fim - inicio, memoria_usada

def criar_tabela_hash(dados):
    tabela = {i: item for i, item in enumerate(dados)}
    return tabela

def criar_pilha(dados):
    pilha = list(dados)
    return pilha

def criar_fila(dados):
    fila = deque(dados)
    return fila

def obter_elementos(estrutura, indices):
    return [estrutura[i] if isinstance(estrutura, dict) else estrutura[i] for i in indices]

arquivo_listagem = "listagem.txt"
arquivos = carregar_arquivo(arquivo_listagem)
indices = [1, 100, 1000, 5000, len(arquivos) - 1]

for nome, func in [("Tabela Hash", criar_tabela_hash), 
                   ("Pilha", criar_pilha), 
                   ("Fila", criar_fila)]:
    estrutura, tempo, memoria = medir_performance(func, arquivos)
    print(f"Tempo para criar {nome} = {tempo:.6f}s, Memória consumida = {memoria} bytes")
    
    elementos, tempo_rec, memoria_rec = medir_performance(obter_elementos, estrutura, indices)
    print(f"Tempo para recuperar itens da {nome} = {tempo_rec:.6f}s, Memória consumida = {memoria_rec} bytes\n")
