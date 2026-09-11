/*
(DESAFIO) Escreva um programa que receba duas strings, como parâmetros de entrada, e informe qual é a maior substring existente nas duas strings. Por exemplo, se as strings de entrada são ACCTGAACTCCCCCC e ACCTAGGACCCCCC, então a maior substring existente entre as duas strings será CCCCCC: char * maior_sub (char *str1, char *str2).
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* maior_sub (char* str1, char* str2){
    int len1 = strlen(str1), len2 = strlen(str2);
    int max_len = 0, id_str = 0;

    for (int i = 0; i < len1; i++) {
        for (int j = 0; j < len2; j++) {
            int k = 0;

            while ((i + k < len1) && (j + k < len2) && (str1[i + k] == str2[j + k])) {
                k++;
            }

            if (k > max_len) {
                max_len = k;
                id_str = i;
            }
        }
    }

    char* maior_substring = malloc((max_len+1)*sizeof(char));

    if (max_len > 0) {
        strncpy(maior_substring, &str1[id_str], max_len);
    }
    maior_substring[max_len] = '\0';

    return maior_substring;
}

int main(void) {
    printf("Maior Substring Comum\n");

    char* str1 = malloc(1024 * sizeof(char));
    char* str2 = malloc(1024 * sizeof(char));
    printf("Insira as duas strings:\n");
    scanf(" %s %s", str1, str2);
    str1 = realloc(str1, (strlen(str1) + 1) * sizeof(char));
    str2 = realloc(str2, (strlen(str2) + 1) * sizeof(char));

    char* sub = maior_sub(str1, str2);

    printf("Maior substring comum: %s", sub);

    free(str1);
    free(str2);
    free(sub);
    return 0;
}