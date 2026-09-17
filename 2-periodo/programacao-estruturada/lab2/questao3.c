// (3) Implemente um programa que derive polinômios. Cada polinômio é definido por um vetor de coeficientes. Por exemplo, o polinômio de grau dois 3x^2 + 2x + 12 terá um vetor de coeficientes v = {12, 2, 3}. Sua derivada será D = {2, 6}, o que equivale ao polinômio 6x + 2. O programa deve,infinitamente: (a) receber o valor do maior grau g do polinômio, seguido de (g + 1) coeficientes; (b) calcular a derivada do polinômio informado, usando a função void derivada(int *poli, int n, int* vet_derivada); e (c) imprimir os novos polinômios na tela. Este programa é válido somente quando o grau g do polinômio for menor ou igual a zero.

#include <stdio.h>
#include <stdlib.h>

void derivada(int *poli, int n, int *vet_derivada) {
    for (int i = 1; i <= n; i++) {
        vet_derivada[i-1] = poli[i] * i;
    }
}

void print_polinomio(int *poli, int grau) {
    int primeiro_termo = 1;
    for (int i = grau; i >= 0; i--) {
        if (poli[i] != 0) {
            if (!primeiro_termo && poli[i] > 0) printf(" + ");
            else if (!primeiro_termo && poli[i] < 0) printf(" - ");
            else if (primeiro_termo && poli[i] < 0) printf("-");

            int valor_abs = poli[i] < 0 ? -poli[i] : poli[i];

            if (i > 1) {
                printf("%dx^%d", valor_abs, i);
            } else if (i == 1) {
                printf("%dx", valor_abs);
            } else {
                printf("%d", valor_abs);
            }
            primeiro_termo = 0;
        }
    }
    if (primeiro_termo) printf("0");
}

int main(void) {
    printf("Calculadora de Derivada\n");
    
    while (1) {
        int g;
        printf("Insira o grau do polinômio: ");
        scanf("%d", &g);
        if (g < 0) {
            break;
        }

        int *poli = malloc((g + 1) * sizeof(int));
        for (int i = 0; i < (g + 1); i++) {
            printf("Insira o coeficiente do termo de grau %d: ", i);
            scanf("%d", &poli[i]);
        }
        
        int *vet_derivada = malloc(g * sizeof(int));
        derivada(poli, g, vet_derivada);

        printf("Polinômio original: ");
        print_polinomio(poli, g);
        printf("\n");

        printf("Derivada: ");
        print_polinomio(vet_derivada, g - 1);
        printf("\n\n");
    }
    return 0;
}