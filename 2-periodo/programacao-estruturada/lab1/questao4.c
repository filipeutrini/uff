// (4) Implemente um programa que, infinitamente, leia um número n e retorne todos os seus divisores. Esse programa para quando n < 2;

#include <stdio.h>

int main(void) {
    printf("Divisores de um Número\n");
    while (1) {
        int n;
        printf("Insira um número: ");
        scanf("%d", &n);
        if (n < 2) break;

        printf("Divisores: 1, ");
        for (int i = 2; i <= (n / 2); i++) {
            if (n % i == 0) {
                printf("%d, ", i);
            }
        }
        printf("%d\n\n", n);
    }
    return 0;
}