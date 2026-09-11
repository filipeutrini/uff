/*
Q1) Implemente um programa que, infinitamente, receba, como parâmetro de entrada, um número n e retorne os n primeiros números primos existentes. Seu programa para quando n for menor ou igual a zero.
*/

#include <stdio.h>

int eh_primo(int num) {
    if (num < 2) return 0;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int n;

    while (1) {
        scanf("%d", &n);

        if (n <= 0) {
            break;
        }

        int contador = 0;
        int num = 2;

        while (contador < n) {
            if (eh_primo(num)) {
                printf("%d ", num);
                contador++;
            }
            num++;
        }
        printf("\n");
    }

    return 0;
}
