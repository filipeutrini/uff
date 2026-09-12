# 1) def criar_lista_vazia():
# retorna uma lista vazia
def criar_lista_vazia():
    return []

# 2) def criar_lista_inicializada(n,valor):
# cria uma lista com n ocorrências de valor
def criar_lista_inicializada(n, valor):
    return [valor] * n

# 3) def imprimir_lista(l):
# imprime os elementos de l
def imprimir_lista(l):
    print(l)

# 4) def buscar_lista(l,valor):
# retorna o indice da primeira ocorrência de valor ou -1 caso não exista
def buscar_lista(l, valor):
    for i in range(len(l)):
        if l[i] == valor:
            return i
    return -1

# 5) def buscar_ocorrencias_lista(l,valor):
# retorna uma lista contendo todas posições onde valor é encontrado em l
def buscar_ocorrencias_lista(l, valor):
    posicoes = []
    for i in range(len(l)):
        if l[i] == valor:
            posicoes.append(i)
    return posicoes

# 6) def insere_lista(l,indice, valor):
# insere valor na posição dado por indice (indice deve ser no máximo igual a len(l))
# sem criar uma nova lista
def insere_lista(l, indice, valor):
    if 0 <= indice <= len(l):
        l.insert(indice, valor)

# 7) def insere_lista_final(l,valor):
# insere valor no final da lista sem criar uma nova
def insere_lista_final(l, valor):
    l.append(valor)

# 8) def insere_lista_inicio(l, valor):
# insere valor no início da lista sem criar uma nova
def insere_lista_inicio(l, valor):
    l.insert(0, valor)

# 9) def remove_lista(l,valor):
# remove valor de l caso exista sem criar uma nova
def remove_lista(l, valor):
    if valor in l:
        l.remove(valor)

# 10) def remove_elemento_lista(l,indice):
# remove o elemento na posição índice e o retorna
def remove_elemento_lista(l, indice):
    if 0 <= indice < len(l):
        return l.pop(indice)
    return None

# 11) def remove_ocorrencias_lista(l,valor):
# remove todas as ocorrências de valor em l
def remove_ocorrencias_lista(l, valor):
    while valor in l:
        l.remove(valor)

# 12) def concatena_listas (l1,l2):
# concatena duas listas
def concatena_listas(l1, l2):
    return l1 + l2

# 13) def selection_sort(l):
# ordena a lista através do método Selection Sort
def selection_sort(l):
    n = len(l)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if l[j] < l[min_idx]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]

# 14) def insertion_sort(l):
# ordena a lista através do método Insertion Sort
def insertion_sort(l):
    for i in range(1, len(l)):
        chave = l[i]
        j = i - 1
        while j >= 0 and l[j] > chave:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = chave

# 15) def combina_listas(l1,l2):
# recebe duas listas ordenadas e retorna uma nova lista ordenada com todos os elementos de l1 e l2
def combina_listas(l1, l2):
    resultado = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            resultado.append(l1[i])
            i += 1
        else:
            resultado.append(l2[j])
            j += 1
    
    # Adiciona os elementos restantes, se houver
    while i < len(l1):
        resultado.append(l1[i])
        i += 1
    while j < len(l2):
        resultado.append(l2[j])
        j += 1
        
    return resultado

# 16) def sublista(l,inicio,fim):
# retorna uma sublista contendo os elementos de l da posição início até a posição fim
def sublista(l, inicio, fim):
    return l[inicio:fim + 1]

# 17) def inclui(l1,l2):
# retorna True se l2 está contida em l1 e False caso contrário
def inclui(l1, l2):
    if not l2:
        return True
    
    len_l1, len_l2 = len(l1), len(l2)
    for i in range(len_l1 - len_l2 + 1):
        if l1[i:i + len_l2] == l2:
            return True
    return False

# 18) def remove_duplicatas(l1):
# retorna uma nova lista com os elementos de l1 sem repetição
def remove_duplicatas(l1):
    nova_lista = []
    for item in l1:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

# 19) def inverte_lista(l1):
# inverte a sequência dos elementos de uma lista sem criar uma nova
def inverte_lista(l1):
    inicio = 0
    fim = len(l1) - 1
    while inicio < fim:
        l1[inicio], l1[fim] = l1[fim], l1[inicio]
        inicio += 1
        fim -= 1

# 20) def duplicar_lista(l1):
# retorna uma cópia de l1
def duplicar_lista(l1):
    return l1.copy()

# 21) def testar_funcoes():
# função de teste que testa todas as funções no módulo
def testar_funcoes():
    l_vazia = criar_lista_vazia()
    l_inicializada = criar_lista_inicializada(10, 0)
    print("Lista vazia:", l_vazia)
    print("Lista inicializada:", l_inicializada)

    print("Imprimir: ", end="")
    imprimir_lista(l_inicializada)

    lista = [1, 3, 2, 3, 4, 5]
    print("Índice do primeiro:", buscar_lista(lista, 3))
    print("Índices de todas ocorrências:", buscar_ocorrencias_lista(lista, 3))

    insere_lista(lista, 2, 99)
    print("Inserir na pos 2:", lista)
    insere_lista_final(lista, 88)
    print("Inserir no final:", lista)
    insere_lista_inicio(lista, 77)
    print("Inserir no início:", lista)

    remove_lista(lista, 99)
    print("Remover elemento:", lista)
    removido = remove_elemento_lista(lista, 0)
    print(f"Elemento removido da pos 0: {removido}, Lista: {lista}")
    remove_ocorrencias_lista(lista, 5)
    print("Remover todas ocorrências de 5:", lista)

    a = [1, 2]
    b = [3, 4]
    print("Concatena listas:", concatena_listas(a, b))

    l_sort1 = [4, 2, 1, 5, 3]
    l_sort2 = [9, 6, 8, 7, 0]
    selection_sort(l_sort1)
    insertion_sort(l_sort2)
    print("Selection Sort:", l_sort1)
    print("Insertion Sort:", l_sort2)

    print("Combina listas ordenadas:", combina_listas(l_sort1, l_sort2))

    sub = sublista([10, 20, 30, 40, 50], 1, 3)
    print("Sublista:", sub)

    print("Contém sublista:", inclui([10, 20, 30, 40], [20, 30]))

    print("Remover duplicatas:", remove_duplicatas([1, 2, 2, 3, 1]))

    l_inv = [1, 2, 3, 4]
    inverte_lista(l_inv)
    print("Lista invertida:", l_inv)

    copia = duplicar_lista(l_inv)
    print("Cópia:", copia)



if __name__ == "__main__":
    testar_funcoes()