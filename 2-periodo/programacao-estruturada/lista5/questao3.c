/*
Q3) A matriz de Hadamard H(N), usada em projetos de programas corretores de erros, é uma matriz N por N, onde N é potência de dois, de elementos booleanos (isto é, elementos 0 e 1) que satisfaz a seguinte propriedade: dadas duas linhas distintas i e j, onde 0 <= i < N e 0 <= j < N, desta matriz, a quantidade de elementos distintos nestas linhas é sempre igual a N/2. Abaixo exemplica-se H(1), H(2) e H(4).

H(1) | H(2) | H(4)
-----------+--------+------------
1   |   1 1 |   1 1 1 1
    |   1 0 |   1 0 1 0
            |   1 1 0 0
            |   1 0 0 1

Para construir H(M), onde M = 2 * N, divide-se a matriz H(M) em quatro partes iguais, chamadas de quadrantes, repete-se três vezes a matriz H(N) nos quadrantes de menores índices, e no quadrante de maiores índices de H(M), inverte-se a matriz H(N). Implemente um programa que imprima a matriz H(N) na console. A dimensão desta matriz deve ser lida pelo seu programa.
*/

#include <stdio.h>
#include <stdlib.h>

void libera_matriz(int** matriz, int lin) {
    for (int i = 0; i < lin; i++) {
        free(matriz[i]);
    }
    free(matriz);
}

int** H(int tam) {
    int** hadamard = (int**) malloc(tam * sizeof(int*));
    for (int i = 0; i < tam; i++) {
        hadamard[i] = malloc(tam * sizeof(int));
    }

    if (tam == 1) {
        hadamard[0][0] = 1;
        return hadamard;
    }

    int metade = tam / 2;
    int** anterior = H(metade);

    for (int i = 0; i < (tam / 2); i ++) {
        for (int j = 0; j < (tam / 2); j++) {
            int valor = anterior[i][j];

            hadamard[i][j] = anterior[i][j];
            hadamard[i][j + metade] = anterior[i][j];
            hadamard[i + metade][j] = anterior[i][j];
            hadamard[i + metade][j + metade] = (valor == 1) ? 0 : 1;
        }
    }
    libera_matriz(anterior, metade);
    return hadamard;
}

void imprime_matriz(int** matriz, int lin, int col) {
    if (matriz == NULL) {
        printf("Matriz vazia.");
        return;
    }

    for (int i = 0; i < lin; i++) {
        for (int j = 0; j < col; j++) {
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }
}

int main(void) {
    printf("Gerador de Matriz de Hadamard\n");

    int tam;
    printf("Insira o tamanho da matriz de Hadamard que deseja (potência de 2): ");
    scanf("%d", &tam);

    if (tam < 1) {
        printf("Deve ser um número positivo.");
        return 1;
    }

    int** hadamard = H(tam);
    imprime_matriz(hadamard, tam, tam);
}