// (2) Implemente um programa que, infinitamente, leia dois números x e y e retorne o MDC entre eles. Esse programa para quando x,y ≤ 1;

#include <stdio.h>

int main(void) {
    printf("Calculadora de MDC\n");
    while (1) {
        int x, y, menor, mdc = 1;
        printf("Insira dois números: ");
        scanf("%d %d", &x, &y);
        if ((x <= 1) && (y <= 1)) break;

        menor = (x < y) ? x : y;
        for (int i = 2; i < (menor / 2); i++) {
            if ((x % i == 0) && (y % i == 0)) mdc = i;
        }
        if ((x % menor == 0) && (y % menor == 0)) mdc = menor;

        printf("MDC(%d, %d) = %d\n\n", x, y, mdc);
    }
    return 0;
}