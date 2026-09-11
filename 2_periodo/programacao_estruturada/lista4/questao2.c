/*
(Q2) Implemente uma função em C que receba uma string como parâmetro e retorne uma nova string com todos os caracteres minúsculos substituídos pelo caracter ‘?’. Por exemplo, se for passada a string “740-Charitas-Leme”, a função deve retornar a string “740-Ch?r?t?s-L?m?”. A assinatura desta função deve ser char * codifica (char *str). A string passada como parâmetro não pode ser alterada. O espaço de memória para a nova string deve ser alocado dinamicamente.
*/
// Pelo exemplo da questão, eu creio que o enunciado correto seja para substituir as VOGAIS MINÚSCULAS por '?'.

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* codifica (char* str) {
    char* codificada = malloc((strlen(str) + 1) * sizeof(char));

    for (int i = 0; i < strlen(str); i++) {
        if ((str[i] == 'a') || (str[i] == 'e') || (str[i] == 'i') || (str[i] == 'o') || (str[i] == 'u')) codificada[i] = '?';
        else codificada[i] = str[i];
    }
    codificada[strlen(str)] = '\0';

    return codificada;
}

int main(void) {
    printf("Codificador de Strings\n");

    char string[100];
    printf("Insira a string a ser codificada: ");
    scanf("%s", &string);

    char* codificada = codifica(string);
    printf("String codificada: %s", codificada);

    free(codificada);
    return 0;
}