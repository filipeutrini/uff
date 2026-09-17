// (2) Retirar todos os múltiplos de k de um vetor de inteiros. Se o seu vetor é composto por {2, 3, 5, 4, 6, 8, 7, 9, 1}, com tamanho 9, e k = 2, seu vetor deve se transformar em {3, 5, 7, 9, 1}, com tamanho igual a 5.  O protótipo dessa função é o seguinte: void retira_mult_k(int *vet, int *novo_tam_vet, int k). NÃO PODEMOS CRIAR VETORES AUXILIARES PRA RESOLVER ESSA QUESTÃO: USE SOMENTE ÍNDICES!!!

#include <stdio.h>
#include <stdlib.h>

void retira_mult_k(int *vet, int *novo_tam_vet, int k) {
    int pos = 0;

    for (int i = 0; i < *novo_tam_vet; i++) {
        if (vet[i] % k != 0) {
            vet[pos] = vet[i];
            pos++;
        }
    }

    *novo_tam_vet = pos;
}

int main(void) {
    printf("Retirar Múltiplos do Vetor\n");

    int tam = 9;
    int vet[9] = {2, 3, 5, 4, 6, 8, 7, 9, 1};
    int k = 2;
    int *tam_vet = &tam, *vetor = &vet[0];

    retira_mult_k(vetor, tam_vet, k);

    printf("Vetor novo: {");
    for (int i = 0; i < tam; i++) {
        if (i != tam - 1) {
            printf("%d, ", vet[i]);
        } else {
            printf("%d}\n", vet[i]);
        }
    }

    return 0;
}