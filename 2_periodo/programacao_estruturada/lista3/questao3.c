/*
Q3) Um número a é dito permutação de um número b se os dígitos de a formam uma permutação dos dígitos de b. Exemplo: 5412434 é uma permutação de 4321445, mas não é uma permutação de 4312455. Faça um programa que receba a e b e responda se a é permutação de b. Obs.: Considere que o dígito 0 (zero) não deve aparecer nos números.
*/

#include <stdio.h>

int eh_permutacao(int a, int b) {
    int algA[9] = {0}, algB[9] = {0};

    while (a > 0) {
        int algarismo = a%10;
        a = (int) a/10;
        algA[algarismo-1] += 1;
    }
    while (b > 0) {
        int algarismo = b%10;
        b = (int) b/10;
        algB[algarismo-1] += 1;
    }

    for (int i = 0; i < 9; i++) {
        if (algA[i] != algB[i]) return 0;
    }
    return 1;
}

int main(void) {
    printf("Conferidor de Permutação\n");

    int a, b;
    printf("Insira dois números (que não incluam o algarismo 0): ");
    scanf("%d %d", &a, &b);

    if (eh_permutacao(a,b)) printf("É permutação.");
    else printf("Não é permutação");
}
