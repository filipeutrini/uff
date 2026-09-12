import math
import random

# 1) Escreva uma função que crie uma matriz de inteiros de ordem m x n, contendo valores aleatórios entre 0 e k.
def criar_matriz_aleatoria(m, n, k):
    return [[random.randint(0, k) for _ in range(n)] for _ in range(m)]

# 2) Escreva uma função em Python que receba uma matriz A e retorne a sua cópia.
def copiar_matriz(A):
    return [linha[:] for linha in A]

# 3) Escreva uma função que receba uma matriz de float A de ordem n x m, e verifique se ela é diagonal dominante, isto é, se o valor de cada elemento na diagonal principal é maior que a soma da magnitude dos elementos na linha a que ele pertence.
def eh_diagonal_dominante(A):
    n = len(A)
    m = len(A[0])
    limite = min(n, m)

    for i in range(limite):
        elem_diagonal = abs(A[i][i])
        soma_outros = sum(abs(A[i][j]) for j in range(m) if j != i)
        if elem_diagonal <= soma_outros:
            return False
    return True

# 4) Escreva uma função em Python que receba uma matriz A e um vetor b, ambos de float, e retorne seu produto.
def produto_matriz_vetor(A, b):
    m = len(A)
    n = len(A[0])
    if len(b) != n:
        return "O tamanho de b deve ser igual ao número de colunas de A."

    resultado = [0.0] * m
    for i in range(m):
        resultado[i] = sum(A[i][j] * b[j] for j in range(n))
    return resultado

# 5) Escreva uma função em Python que receba duas matrizes A e B, ambas de float, e retorne seu produto.
def produto_matrizes(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B)
    q = len(B[0])

    if n != p:
        return "O número de colunas de A deve ser igual ao número de linhas de B."

    AB = [[0.0 for _ in range(q)] for _ in range(m)]
    for i in range(m):
        for j in range(q):
            AB[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return AB


# 6) Escreva uma função em Python que receba uma matriz A de inteiros e determine os índices (i,j) dos elementos que são maiores que todos os demais em uma vizinhança 3x3 em torno do sua posição (i,j).
def maximos_locais_3x3(A):
    m = len(A)
    n = len(A[0])
    indices = []

    for i in range(m):
        for j in range(n):
            valor_atual = A[i][j]
            eh_maximo = True

            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        if A[ni][nj] >= valor_atual:
                            eh_maximo = False
                            break
                if not eh_maximo:
                    break

            if eh_maximo:
                indices.append((i, j))

    return indices

# 7) Escreva uma função em Python que receba uma matriz de caracteres A de ordem nxm e uma lista de palavras L. A função deve retornar uma nova lista contendo todas as tuplas (i,j) que descrevem a posição da primeira letra de todas as palavras que estejam incluídas em alguma linha ou coluna da matriz.
def buscar_palavras_matriz(A, L):
    n = len(A)
    m = len(A[0])
    posicoes = set()

    linhas_str = ["".join(A[i]) for i in range(n)]
    colunas_str = ["".join(A[i][j] for i in range(n)) for j in range(m)]

    for palavra in L:
        for i in range(n):
            linha = linhas_str[i]
            pos = linha.find(palavra)
            while pos != -1:
                posicoes.add((i, pos))
                pos = linha.find(palavra, pos + 1)

        for j in range(m):
            coluna = colunas_str[j]
            pos = coluna.find(palavra)
            while pos != -1:
                posicoes.add((pos, j))
                pos = coluna.find(palavra, pos + 1)

    return list(posicoes)

# 8) Escreva um programa em Python que receba uma matriz de ordem n x m representada por um array M de tamanho n*m e um par de índices (i,j) e retorne o elemento correspondente na posição (i,j) da matriz.
def obter_elemento_flat(M, n, m, i, j):
    if not (0 <= i < n and 0 <= j < m):
        return "Índices fora da matriz."
    indice_linear = i * m + j
    return M[indice_linear]

# 9) Escreva uma função que receba uma lista L contendo valores inteiros entre 0 e k, e produza uma matriz M de ordem n x n, onde n = ceil(sqrt(len(L))), cujos valores na linha M[i] são gerados aleatoriamente entre 0 e L[i].
def gerar_matriz_por_limites(L):
    tam = len(L)
    n = math.ceil(math.sqrt(tam))
    M = []

    for i in range(n):
        limite = L[i] if i < tam else 0
        linha = [random.randint(0, max(0, limite)) for _ in range(n)]
        M.append(linha)

    return M

# 10) Escreva uma função que receba uma matriz de inteiros e produza um array histograma, tal que, para cada elemento distinto A[i][j], histograma[A[i][j]] contém a frequência com o qual A[i][j] ocorre em A.
def calcular_histograma(A):
    if not A or not A[0]:
        return []

    max_val = max(max(linha) for linha in A)
    histograma = [0] * (max_val + 1)

    for linha in A:
        for valor in linha:
            if valor >= 0:
                histograma[valor] += 1

    return histograma

# 11) Escreva uma função em Python que receba duas matrizes A e B de inteiros, de ordem n x m e p x q, respectivamente, e calcule o produto de Kronecker A (x) B.
def produto_kronecker(A, B):
    n, m = len(A), len(A[0])
    p, q = len(B), len(B[0])

    resultado = [[0] * (m * q) for _ in range(n * p)]

    for i in range(n):
        for j in range(m):
            for k in range(p):
                for l in range(q):
                    resultado[i * p + k][j * q + l] = A[i][j] * B[k][l]

    return resultado

# 12) Escreva uma função em Python que receba uma matriz A de ordem m x n e retorne uma submatriz contendo os elementos de A iniciando no índice (i,j) e terminando no índice (k,l), onde 0 <= i, k < m e 0 <= j, l < n.
def extrair_submatriz(A, i, j, k, l):
    m, n = len(A), len(A[0])

    i_min, i_max = min(i, k), max(i, k)
    j_min, j_max = min(j, l), max(j, l)

    i_min = max(0, i_min)
    i_max = min(m - 1, i_max)
    j_min = max(0, j_min)
    j_max = min(n - 1, j_max)

    submatriz = []
    for r in range(i_min, i_max + 1):
        submatriz.append(A[r][j_min : j_max + 1])

    return submatriz

# 13) Escreva uma função em Python que receba uma matriz A de ordem m x n, e uma matriz B de ordem p x q, onde p <= m e q <= n e verifique se B está contida em A.
def contem_submatriz(A, B):
    m, n = len(A), len(A[0])
    p, q = len(B), len(B[0])

    if p > m or q > n:
        return False

    for i in range(m - p + 1):
        for j in range(n - q + 1):
            contem = True
            for r in range(p):
                for c in range(q):
                    if A[i + r][j + c] != B[r][c]:
                        contem = False
                        break
                if not contem:
                    break
            if contem:
                return True
    return False

# 14) Escreva uma função em Python que receba uma matriz A de valores booleanos de ordem n x n e uma lista de índices I, onde os valores armazenados em I são inteiros de 0 a n-1. Cada índice da matriz A representa uma localidade e o valor armazenado em um elemento A[i][j] indica se há um caminho conectando i a j. A função deve retornar verdadeiro se existe um caminho passando por todas as localidades descritas em I ou falso, caso contrário.
def existe_caminho(A, I):
    if len(I) <= 1:
        return True

    for k in range(len(I) - 1):
        origem = I[k]
        destino = I[k + 1]
        if not A[origem][destino]:
            return False

    return True


# 15) Escreva uma função em Python que receba uma matriz A de ordem m x n e uma matriz B, de ordem k x k, e calcule a convolução M = A * B.
def convolucao_2d(A, B):
    m, n = len(A), len(A[0])
    k_size = len(B)
    pad = k_size // 2

    M = [[0.0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            soma = 0.0
            for u in range(k_size):
                for v in range(k_size):
                    img_i = i - (u - pad)
                    img_j = j - (v - pad)

                    if 0 <= img_i < m and 0 <= img_j < n:
                        soma += A[img_i][img_j] * B[u][v]
            M[i][j] = soma

    return M



if __name__ == "__main__":
    m1 = criar_matriz_aleatoria(3, 4, 10)
    print("Matriz aleatória:", m1)

    m2 = copiar_matriz(m1)
    print("Cópia da matriz:", m2)

    mat_diag = [[5.0, 1.0, 2.0], [1.0, 4.0, 1.0], [0.0, 2.0, 3.0]]
    print("Diagonal Dominante?", eh_diagonal_dominante(mat_diag))

    A_vet = [[1.0, 2.0], [3.0, 4.0]]
    vet_b = [5.0, 6.0]
    print("Matriz x Vetor:", produto_matriz_vetor(A_vet, vet_b))

    mA = [[1.0, 2.0], [3.0, 4.0]]
    mB = [[2.0, 0.0], [1.0, 2.0]]
    print("Produto:", produto_matrizes(mA, mB))

    m_viz = [[1, 2, 3], [4, 9, 5], [6, 7, 8]]
    print("Máximo local:", maximos_locais_3x3(m_viz))

    char_mat = [["c", "a", "s", "a"], ["o", "x", "y", "z"], ["l", "a", "g", "o"]]
    palavras = ["casa", "lago", "sol"]
    print("Início das palavras encontradas:", buscar_palavras_matriz(char_mat, palavras))

    M_flat = [10, 20, 30, 40, 50, 60]
    print("Elemento na pos (1,1) de [2x3]:", obter_elemento_flat(M_flat, 2, 3, 1, 1))

    lista_lim = [2, 5, 10]
    print("Matriz por limites da lista:", gerar_matriz_por_limites(lista_lim))

    mat_hist = [[1, 2, 2], [3, 1, 0], [2, 3, 3]]
    print("Histograma:", calcular_histograma(mat_hist))

    kA = [[1, 2], [3, 4]]
    kB = [[0, 5], [6, 7]]
    print("Produto de Kronecker:", produto_kronecker(kA, kB))

    mat_sub = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Submatriz:", extrair_submatriz(mat_sub, 0, 0, 1, 1))

    mat_grande = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat_peq = [[5, 6], [8, 9]]
    print("B contida em A?", contem_submatriz(mat_grande, mat_peq))

    a = [
        [True, True, False],
        [False, True, True],
        [True, False, True],
    ]
    i = [0, 1, 2]
    print("Existe caminho?", existe_caminho(a, i))

    img = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    kernel = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
    print("Convolução 2D de imagem x kernel:")
    res_conv = convolucao_2d(img, kernel)
    for linha in res_conv:
        print(linha)