// (1) Escreva uma função que ordene os caracteres de uma String, considerando seus respectivos valores na tabela ASCII. Se sua string for "amoR", a resposta será "Ramo". O protótipo dessa função é o seguinte: void ordena(char *str). NÃO PODEMOS CRIAR VETORES E STRINGS AUXILIARES PRA RESOLVER ESSA QUESTÃO!!!

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compara_letras(const void *a, const void *b) {
    if (*(char*) a < *(char*) b) return -1;
    if (*(char*) a > *(char*) b) return 1;
    return 0;
}

void ordena(char *str) {
    qsort(str, strlen(str), sizeof(char), compara_letras);
}

int main(void) {
    printf("Ordenador de String\n");

    char* string = malloc(1024 * sizeof(char));
    printf("Insira a string a ser ordenada: ");
    scanf("%s", string);
    string = realloc(string, strlen(string) + 1);

    ordena(string);

    printf("%s\n", string);

    return 0;
}