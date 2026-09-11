/*
Q2) Implemente um programa que, infinitamente, teste se um número é um palíndromo (Dica: se uma palavra pode ser lida, indiferentemente, da esquerda para a direita e vice-versa, ela é considerada um palíndromo). Você deve passar o número a ser testado. O seu programa deverá imprimir as seguintes mensagens “VERDADEIRO” (caso o número seja um palíndromo) ou “FALSO” (caso o número não seja um palíndromo) na console. Seu programa para quando o número for negativo.
*/

#include <stdio.h>

int eh_palindromo(int n) {
    int numero = n, inverso = 0;
    while (numero > 0) {
        inverso = (inverso * 10) + (numero % 10);
        numero = (int) numero / 10;
    }
    if (n == inverso) return 1;
    return 0;
}

int main(void) {
    printf("Teste de Palindromo\n");
    while (1) {
        int num;
        printf("Insira um número: ");
        scanf("%d", &num);
        if (num < 0) break;

        if (eh_palindromo(num)) printf("VERDADEIRO\n");
        else printf("FALSO\n");
    }
    return 0;
}
