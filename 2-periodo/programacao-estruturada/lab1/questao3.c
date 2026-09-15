// (3) Implemente um programa que, infinitamente, leia um número n e retorne o n-ésimo termo da sequência de Fibonacci, sabendo-se que fib(0) = 1 e fib(1) = 1. Esse programa para quando n < 0;

#include <stdio.h>

int fib(int n) {
    if ((n == 0) || (n == 1)) return 1;
    int a = 1, b = 1, fibonacci;

    for (int i = 1; i < n; i++) {
        fibonacci = a + b;
        a = b;
        b = fibonacci;
    }

    return fibonacci;
}

int main(void) {
    printf("Termo da Sequência de Fibonacci\n");
    
    while (1) {
        int n;
        printf("Insira o número do termo que deseja: ");
        scanf("%d", &n);
        if (n < 0) break;

        int termo = fib(n);
        printf("O termo %d da sequência de Fibonacci é: %d\n\n", n, termo);
    }
    return 0;
}