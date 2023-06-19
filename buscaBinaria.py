def buscaBinaria (valorBuscado, estrutura):
    inicio = 0
    fim = len(estrutura) - 1
    while inicio <= fim: 
        meio = int((inicio+ fim) / 2)
        if estrutura[meio] == valorBuscado: return meio 
        if estrutura[meio] < valorBuscado: inicio = meio + 1
        else: fim = meio - 1
    return -1