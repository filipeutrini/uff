/*
Q1) Alguns números possuem uma propriedade interessante: se você recuperar seus dois primeiros dı́gitos e seus dois últimos dı́gitos e elevar ao quadrado a soma deles, você obterá a concatenação desses quatro dı́gitos. Por exemplo, o número 203125 possui essa propriedade, pois (20 + 25)² = 2025. Por outro lado, o mesmo não é observado para 20326, pois (20 + 26)² = 2116 ≠ 2026. Escreva uma função que informa se um número possui essa propriedade – int teste(int n) – retornando UM se o número satisfaz a essa propriedade, e ZERO caso contrário.
*/

#include <stdio.h>

int teste(int n) {
    if (n < 1000) return 0;

    int ultimos_digitos = n % 100;
    while (n > 99) {
        n = (int) n / 10;
    }
    if ((n+ultimos_digitos)*(n+ultimos_digitos) == (n*100)+ultimos_digitos) return 1;
    return 0;
}

int main(void) {
    printf("Testar Propriedade\n");
    int num;
    printf("Insira um número: ");
    scanf("%d", &num);

    printf("%d\n", teste(num));
    return 0;
}
