// (5) Implemente um programa que, infinitamente, receba como parâmetro de entrada um número n e retorne todos os primos menores ou iguais a n. Seu programa para quando n < 2.

#include <stdio.h>

int main(void) {
    printf("Números Primos até N\n");
    while (1) {
        int n;
        printf("Insira um número: ");
        scanf("%d", &n);
        if (n < 2) break;

        for (int i = 2; i <= n; i++) {
            int div = 0;
            for (int j = 2; j <= (i / 2); j++) {
                if (i % j == 0) {
                    div++;
                    break;
                }
            }
            if (div == 0) {
                printf("%d ", i);
            }
        }
        printf("\n\n");
    }
}