# 1) Escreva um programa que leia um array de inteiros vet. Implemente uma função que receba um inteiro e retorne a posição de x no array vet, caso ele esteja presente. A função deve retornar -1 caso contrário.
def buscar_elemento(vet, x):
    for i in range(len(vet)):
        if vet[i] == x:
            return i
    return -1

# 2) Escreva uma função que seja capaz de adicionar um elemento x ao final do array de inteiros vet.
def adicionar_no_final(vet, x):
    vet.append(x)
    return vet

# 3) Escreva uma função que seja capaz de adicionar um elemento x no início do array de inteiros vet.
def adicionar_no_inicio(vet, x):
    vet.append(0)
    for i in range(len(vet) - 1, 0, -1):
        vet[i] = vet[i - 1]
    vet[0] = x
    return vet

# 4) Escreva uma função que seja capaz de inserir um elemento em uma posição i do array de inteiros vet, sendo 0 <= i <= |vet|
def inserir_na_posicao(vet, x, i):
    if 0 <= i <= len(vet):
        vet.append(0)
        for j in range(len(vet) - 1, i, -1):
            vet[j] = vet[j - 1]
        vet[i] = x
    return vet

# 5) Escreva uma função que receba um array de inteiros vet e o ordene segundo o método da bolha.
def ordenacao_bolha(vet):
    n = len(vet)
    for i in range(n):
        for j in range(0, n - i - 1):
            if vet[j] > vet[j + 1]:
                vet[j], vet[j + 1] = vet[j + 1], vet[j]
    return vet

# 6) Escreva uma função que insira um elemento no array de inteiros vet mantendo sua ordenação.
def inserir_ordenado(vet, x):
    vet.append(0)
    i = len(vet) - 2
    while i >= 0 and vet[i] > x:
        vet[i + 1] = vet[i]
        i -= 1
    vet[i + 1] = x
    return vet

# 7) Escreva uma função que receba um array de inteiros vet e um valor x, e remova x de vet caso ele esteja presente.
def remover_elemento(vet, x):
    pos = -1
    for i in range(len(vet)):
        if vet[i] == x:
            pos = i
            break
            
    if pos != -1:
        for i in range(pos, len(vet) - 1):
            vet[i] = vet[i + 1]
        vet.pop()
        
    return vet

# 8) Escreva uma função que remova as duplicatas de um array de inteiros vet.
def remover_duplicatas(vet):
    sem_duplicatas = []
    for item in vet:
        if item not in sem_duplicatas:
            sem_duplicatas.append(item)
    return sem_duplicatas

# 9) Escreva uma função que receba dois arrays de inteiros vet1 e vet2 e retorne um novo array contendo os elementos de ambos.
def concatenar_arrays(vet1, vet2):
    return vet1 + vet2

# 10) Escreva uma função que receba dois arrays de inteiros vet1 e vet2, representando dois conjuntos, e retorne um novo array contendo a união dos elementos de vet1 e vet2.
def uniao_conjuntos(vet1, vet2):
    uniao = []
    for elem in vet1 + vet2:
        if elem not in uniao:
            uniao.append(elem)
    return uniao

# 11) Escreva uma função que receba dois arrays de inteiros vet1 e vet2, representando dois conjuntos, e retorne um novo array contendo a interseção dos elementos de vet1 e vet2.
def intersecao_conjuntos(vet1, vet2):
    intersecao = []
    for elem in vet1:
        if elem in vet2 and elem not in intersecao:
            intersecao.append(elem)
    return intersecao

# 12) Escreva uma função que receba dois arrays de inteiros vet1 e vet2, representando dois conjuntos, e retorne um novo array contendo a diferença dos elementos de vet1 e vet2.[cite: 1]
def diferenca_conjuntos(vet1, vet2):
    diferenca = []
    for elem in vet1:
        if elem not in vet2 and elem not in diferenca:
            diferenca.append(elem)
    return diferenca

if __name__ == "__main__":
    vetor = [24, 83, 25, 10, 85, 54, 35, 28, 25, 25, 19, 125, 25, 78, 35, 46, 92, 11, 2, 1]
    vetor2 = [85, 23, 57, 23, 57, 2, 6, 57, 457, 2, 3, 3, 7, 658, 236, 86, 2, 6, 7, 25, 29]

    print(buscar_elemento(vetor, 10))

    vetor = adicionar_no_final(vetor, 15)
    print(vetor)

    vetor = adicionar_no_inicio(vetor, 5)
    print(vetor)

    vetor = inserir_na_posicao(vetor, 37, 4)
    print(vetor)

    vetor = ordenacao_bolha(vetor)
    print(vetor)

    vetor = inserir_ordenado(vetor, 47)
    print(vetor)

    vetor = remover_elemento(vetor, 83)
    print(vetor)

    vetor = remover_duplicatas(vetor)
    print(vetor)

    conc = concatenar_arrays(vetor, vetor2)
    print(conc)

    uniao = uniao_conjuntos(vetor, vetor2)
    print(uniao)

    intersecao = intersecao_conjuntos(vetor, vetor2)
    print(intersecao)

    diferenca = diferenca_conjuntos(vetor, vetor2)
    print(diferenca)