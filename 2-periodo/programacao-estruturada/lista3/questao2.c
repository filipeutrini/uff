/*
Q2) Implemente um programa que integre e derive polinômios. Cada polinômio é definido por um vetor que contém seus coeficientes. Por exemplo, o polinômio de grau dois 3x² + 2x + 12 terá um vetor de coeficientes v = {12,2,3}. Sua integral será I = {0, 12, 1, 1}, equivalente ao polinômio x³ + x²+ 12x, e sua derivada será D = {2, 6}, equivalendo ao polinômio 6x + 2. O programa deve, infinitamente: (a) receber o valor do maior grau g do polinômio, seguido de (g + 1) coeficientes; (b) calcular qual é a integral e a derivada do polinômio informado; e (c) imprimir os novos polinômios na tela. Este programa para somente quando o grau g do polinômio for menor ou igual a zero.
*/

#include <stdio.h>
#include <stdlib.h>

int* derivada(int coeficientes[], int grau) {
    int* coef_derivada = malloc(grau * sizeof(int));
    for (int i = 0; i < grau; i++) {
        coef_derivada[i] = coeficientes[i + 1] * (i + 1);
    }

    return coef_derivada;
}

float* integral(int coeficientes[], int grau) {
    // A integral de um polinômio de grau g tem grau g + 1 (logo, g + 2 coeficientes)
    float* coef_integral = malloc((grau + 2) * sizeof(float));

    coef_integral[0] = 0.0;

    for (int i = 0; i <= grau; i++) {
        coef_integral[i + 1] = (float)coeficientes[i] / (i + 1);
    }

    return coef_integral;
}

void imprime_polinomio_int(int coef[], int grau) {
    int primeiro_termo = 1;
    for (int i = grau; i >= 0; i--) {
        if (coef[i] != 0) {
            if (!primeiro_termo && coef[i] > 0) printf(" + ");
            else if (!primeiro_termo && coef[i] < 0) printf(" - ");
            else if (primeiro_termo && coef[i] < 0) printf("-");

            int valor_abs = coef[i] < 0 ? -coef[i] : coef[i];

            if (i == 0) {
                printf("%d", valor_abs);
            } else if (i == 1) {
                printf("%dx", valor_abs);
            } else {
                printf("%dx^%d", valor_abs, i);
            }
            primeiro_termo = 0;
        }
    }
    if (primeiro_termo) printf("0");
}

void imprime_polinomio_float(float coef[], int grau) {
    int primeiro_termo = 1;
    for (int i = grau; i >= 0; i--) {
        if (coef[i] != 0) {
            if (!primeiro_termo && coef[i] > 0) printf(" + ");
            else if (!primeiro_termo && coef[i] < 0) printf(" - ");
            else if (primeiro_termo && coef[i] < 0) printf("-");

            float valor_abs = coef[i] < 0 ? -coef[i] : coef[i];

            if (i == 0) {
                printf("%.2f", valor_abs);
            } else if (i == 1) {
                printf("%.2fx", valor_abs);
            } else {
                printf("%.2fx^%d", valor_abs, i);
            }
            primeiro_termo = 0;
        }
    }
    if (primeiro_termo) printf("0");
}

int main(void) {
    printf("Calculadora de Polinômios\n");
    while (1) {
        // (a)
        int g;
        printf("Insira o grau do polinômio: ");
        if (scanf("%d", &g) != 1 || g <= 0) break;

        int coeficientes[g + 1];
        for (int i = 0; i <= g; i++) {
            printf("Insira o coeficiente do termo de grau %d: ", i);
            scanf("%d", &coeficientes[i]);
        }

        // (b)
        int* coef_derivada = derivada(coeficientes, g);
        float* coef_integral = integral(coeficientes, g);

        // (c)
        printf("\nPolinômio original: ");
        imprime_polinomio_int(coeficientes, g);
        printf("\n");

        printf("Derivada: ");
        imprime_polinomio_int(coef_derivada, g - 1);
        printf("\n");

        printf("Integral: ");
        imprime_polinomio_float(coef_integral, g + 1);
        printf("\n");

        free(coef_derivada);
        free(coef_integral);
    }

    return 0;
}