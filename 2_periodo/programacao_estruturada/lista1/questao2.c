/*
Q2) Implemente um programa que, infinitamente, receba, como parâmetro de entrada, um número n e retorne os n primeiros números primos existentes depois de n. Por exemplo, se n = 2, a resposta será os primos 3 e 5. É necessário salientar que n não precisa ser primo. Seu programa para quando n for menor ou igual a zero.
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
        int num = n+1;

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
