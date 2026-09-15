/*
Q2) Considere duas matrizes de inteiros de dimensões m1xn1 e m2xn2, onde m1 e n1 representam, respectivamente, o número de linhas e o número de colunas da primeira matriz, e m2 e n2 representam, respectivamente, o número de linhas e o número de colunas da segunda matriz. Escreva uma função que realize a multiplicação destas duas matrizes sem alterar nem a primeira e nem a segunda matriz: int** mult (int m1, int n1, int **mat1, int m2, int n2, int **mat2)
*/

#include <stdio.h>
#include <stdlib.h>

int** mult (int m1, int n1, int **mat1, int m2, int n2, int **mat2) {
    if (n1 != m2) {
        printf("Tamanhos incompatíveis.");
        return NULL;
    }

    int** matriz = (int**) malloc(m1 * sizeof(int*));
    for (int i = 0; i < m1; i++) {
        matriz[i] = (int*) malloc(n2 * sizeof(int));
    }

    for (int i = 0; i < m1; i++) {
        for (int j = 0; j < n2; j++) {
            matriz[i][j] = 0;
            for (int k = 0; k < n1; k++) {
                matriz[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }

    return matriz;
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

void libera_matriz(int** matriz, int lin) {
    for (int i = 0; i < lin; i++) {
        free(matriz[i]);
    }
    free(matriz);
}

int main(void) {
    printf("Multiplicador de Matrizes\n");
    int m1, n1, m2, n2;
    printf("Insira o número de linhas da primeira matriz: ");
    scanf("%d", &m1);
    printf("Insira o número de colunas da primeira matriz: ");
    scanf("%d", &n1);

    int **mat1 = (int**) malloc(m1 * sizeof(int*));
    for (int i = 0; i < m1; i++) {
        mat1[i] = (int*) malloc(n1 * sizeof(int));
    }
    printf("Insira os elementos da primeira matriz: ");
    for (int i = 0; i < m1; i++) {
        for (int j = 0; j < n1; j++) {
            scanf("%d", &mat1[i][j]);
        }
    }

    printf("Insira o número de linhas da segunda matriz: ");
    scanf("%d", &m2);
    printf("Insira o número de colunas da segunda matriz: ");
    scanf("%d", &n2);

    int **mat2 = (int**) malloc(m2 * sizeof(int*));
    for (int i = 0; i < m2; i++) {
        mat2[i] = (int*) malloc(n2 * sizeof(int));
    }
    printf("Insira os elementos da segunda matriz: ");
    for (int i = 0; i < m2; i++) {
        for (int j = 0; j < n2; j++) {
            scanf("%d", &mat2[i][j]);
        }
    }

    int** mat_mult = mult(m1, n1, mat1, m2, n2, mat2);

    if (mat_mult != NULL) {
        printf("\nResultado da multiplicação:\n");
        imprime_matriz(mat_mult, m1, n2);
        libera_matriz(mat_mult, m1);
    } else {
        free(mat_mult);
    }

    libera_matriz(mat1, m1);
    libera_matriz(mat2, m2);

    return 0;
}
