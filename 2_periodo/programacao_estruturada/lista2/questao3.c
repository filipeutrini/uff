/*
Q3) Implemente um programa que, infinitamente, receba, como parâmetro de entrada, um número n e retorne a representação binária de n. Por exemplo, se n é igual a 12, a resposta deste programa deve ser “1100”. Seu programa para quando n for menor que zero.
*/

#include <stdio.h>

int dec_to_bin(int n) {
    int bin = 0, mult = 1;
    while (n > 0) {
        bin = (n % 2) * mult + bin;
        n = (int) n / 2;
        mult *= 10;
    }
    return bin;
}

int main(void) {
    printf("Decimal para Binário\n");
    while (1) {
        int n;
        printf("Insira um número:");
        scanf("%d", &n);
        if (n < 0) break;

        printf("%d\n", dec_to_bin(n));
    }
    return 0;
}
