/*
Q1) Uma forma simples e eficiente de calcular todos os números primos até um certo valor n é o método da Peneira de Eratosthenes. O processo é simples: escrevem-se todos os valores entre 2 e n (limite máximo). Em seguida, faz-se um círculo em volta do 2, marcando como primo e riscam-se todos os seus múltiplos. Continua-se a fazer círculos em volta do menor inteiro que se encontra, eliminando todos os seus múltiplos. Quando não restarem números sem terem círculos à volta ou traços por cima, os números com círculos à volta representam todos os primos até n.
Escreva um programa que implemente a Peneira de Eratosthenes. Você deve ler o valor n e mostrar todos os números primos encontrados.
*/

#include <stdio.h>
int eh_primo(int numero) {
    if (numero <= 1)
        return 0;
    int div = 0;
    for (int i = 2; i <= numero / 2; i++) {
        if (numero % i == 0)
            return 0;
    }
    return 1;
}

void primos_erastosthenes(int n) {
    int vet[n - 2];
    for (int i = 2; i < n; i++) {
        vet[i - 2] = i;
    }
    for (int i = 0; i < n - 2; i++) {
        if (vet[i] != 0) {
            if (eh_primo(vet[i])) {
                for (int j = i + 1; j < n - 2; j++) {
                    if (vet[j] % vet[i] == 0) {
                        vet[j] = 0;
                    }
                }
            }
        }
    }
    for (int i = 0; i < n - 2; i++) {
        if (vet[i] != 0) {
            printf("%d ", vet[i]);
        }
    }
}

int main(void) {
    int n;
    printf("Peneira de Erastosthenes\n");
    printf("Insira um número: ");
    scanf("%d", &n);
    primos_erastosthenes(n);
    return 0;
}
