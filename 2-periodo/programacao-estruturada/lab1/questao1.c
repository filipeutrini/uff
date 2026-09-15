// (1) Implemente um programa que, infinitamente, leia um número n e a sequência de n elementos e retorne o número de vezes em que essa sequência deixou de ser estritamente crescente. Esse programa para quando n ≤ 0;

#include <stdio.h>

int main(void) {
    while (1) {
        int n, counter = 0;
        float numero, anterior;
        printf("Insira o número de elementos: ");
        scanf("%d", &n);
        if (n <= 0) break;

        printf("Insira os elementos:\n");
        scanf("%f", &numero);
        anterior = numero;
        for (int i = 0; i < (n - 1); i++) {
            scanf("%f", &numero);
            if (numero <= anterior) counter++;
            anterior = numero;
        }

        printf("Número de vezes que deixou de ser crescente: %d\n\n", counter);
    }
    return 0;
}