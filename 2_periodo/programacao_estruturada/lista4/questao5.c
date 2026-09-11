/*
(Q5) Escreva uma função que dadas duas strings, retorne UM se a primeira contém a segunda, ignorando maiúsculas e minúsculas, e ZERO, caso contrário. O protótipo da função é o seguinte: int cic (char *str1, char *str2).
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Fiz uma função que transforma letras maíusculas em minúsculas para facilitar a comparação.
char* lower(char* str) {
    char* s = malloc((strlen(str) + 1) * sizeof(char));

    for (int i = 0; i < strlen(str); i++) {
        if ((str[i] >= 65) && (str[i] <= 90)) s[i] = str[i] + 32;
        else s[i] = str[i];
    }
    s[strlen(str)] = '\0';

    return s;
}

int cic(char* str1, char* str2) {
    char* s1 = lower(str1);
    char* s2 = lower(str2);

    int len1 = strlen(s1), len2 = strlen(s2);
    int cont = 0, substring = 0;

    if (len2 <= len1) {
        for (int i = 0; i <= len1 - len2; i++) {
            int j;

            for (j = 0; j < len2; j++) {
                if (s1[i + j] != s2[j]) {
                    break;
                }
            }

            if (j == len2) {
                substring = 1;
                break;
            }
        }
    }
    
    free(s1);
    free(s2);
    return substring;
}

int main(void) {
    printf("Verificador de Substring Não Case-Sensitive\n");

    // Fiz strings de tamanho dinâmico para conseguir comparar direito.
    char* str1 = malloc(1024 * sizeof(char));
    char* str2 = malloc(1024 * sizeof(char));
    printf("Insira a string principal e a string a ser comparada:\n");
    scanf(" %s %s", str1, str2);
    str1 = realloc(str1, (strlen(str1) + 1) * sizeof(char));
    str2 = realloc(str2, (strlen(str2) + 1) * sizeof(char));

    printf("%d", cic(str1, str2));

    free(str1);
    free(str2);

    return 0;
}