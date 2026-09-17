/*
(3) Escreva um programa em C que receba, infinitamente, uma matriz "sem classificação", descubra a classe de cada matriz e as imprima de acordo com a classe a que pertencem. As classes aceitas nesta questão são as seguintes:
-> Linha: formada por uma única linha;
-> Coluna: formada por uma única coluna;
-> Simétrica: ocorre quando o elemento da linha i e coluna j é igual ao elemento da linha j e coluna i, para todos os elementos dessa matriz;
-> Triangular: quando todos os elementos acima, ou abaixo da diagonal principal são iguais a zero (se uma matriz possuir todos os elementos iguais a zero, essa matriz será considerada simétrica);
-> Identidade: ocorre quando os elementos da diagonal principal são todos iguais a um e os demais elementos são iguais a zero;
-> NRA: sem nenhuma das classificações supracitadas.

Seguem alguns exemplos:
ENTRADA        SAÍDA
=====================
2 1        COLUNA        
0
0

1 2        LINHA
0 0

2 2       SIMÉTRICA
1 0
0 7

2 3        NRA
1 2 3
0 0 0

2 2        IDENTIDADE
1 0
0 1

2 2       SIMÉTRICA
1 2
2 0

2 2        TRIANGULAR
1 0
3 4

0 0        SAÍDA DO PROGRAMA
*/

#include <stdio.h>
#include <stdlib.h>

int eh_simetrica(int **mat, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] != mat[j][i]) {
                return 0;
            }
        }
    }
    return 1;
}

int eh_triangular_superior(int **mat, int n) {
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (mat[i][j] != 0) {
                return 0;
            }
        }
    }
    return 1;
}

int eh_triangular_inferior(int **mat, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (mat[i][j] != 0) {
                return 0;
            }
        }
    }
    return 1;
}

int eh_identidade(int **mat, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if ((mat[i][j] != 0) && (i != j)) {
                return 0;
            }
        }
        if (mat[i][i] != 1) return 0;
    }
    return 1;
}

void classifica_matriz(int **mat, int lin, int col) {
    if (col == 1 && lin > 1) {
        printf("COLUNA");
        return;
    }
    
    else if (lin == 1 && col > 1) {
        printf("LINHA");
        return;
    }

    else if (lin == col) {
        if (eh_identidade(mat, lin)) {
            printf("IDENTIDADE");
            return;
        }

        if (eh_simetrica(mat, lin)) {
            printf("SIMETRICA");
            return;
        }

        int triangular_inf = eh_triangular_inferior(mat, lin);
        int triangular_sup = eh_triangular_superior(mat, lin);
        if (triangular_inf || triangular_sup) {
            printf("TRIANGULAR");
            return;
        }
    } else {
        printf("NRA");
    }
}

int main(void) {
    printf("Classificação de Matrizes\n");
    
    while (1) {
        int m, n;
        scanf("%d %d", &m, &n);
        if((m == 0) && (n == 0)) break;

        int **matriz = (int**) malloc(m * sizeof(int*));
        for (int i = 0; i < m; i++) {
            matriz[i] = (int*) malloc(n * sizeof(int));
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                scanf("%d", &matriz[i][j]);
            }
        }

        classifica_matriz(matriz, m, n);

        for (int i = 0; i < m; i++) {
            free(matriz[i]);
        }
        free(matriz);

        printf("\n");
    }
    return 0;
}