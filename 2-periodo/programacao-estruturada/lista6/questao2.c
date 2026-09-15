/*
(Q2) Escreva um procedimento que receba o nome de um arquivo texto, cujo conteúdo são valores inteiros positivo, onde o maior elemento deste arquivo é 1000, e imprima na tela o número de vezes que cada elemento aparece – void resumo(char *Arq).
*/

#include <stdio.h>

void resumo(char *Arq){
    int numeros[1000] = {0};
    
    FILE *entrada = fopen(Arq, "r");
    int numero;

    while(fscanf(entrada, "%d", &numero) == 1) {
        numeros[numero] += 1;
    }

    for (int i = 0; i < 1000; i++) {
        if (numeros[i] != 0) {
            printf("%d: %d vezes\n", i, numeros[i]);
        }
    }
}

int main(int argc, char** argv) {
    if (argc != 2) {
        printf("Erro. A entrada deve ser no formato: <exec> <arq_entrada>. \n");
        return 1;
    }

    char* arq_entrada = argv[1];

    resumo(arq_entrada);
    
    return 0;
}