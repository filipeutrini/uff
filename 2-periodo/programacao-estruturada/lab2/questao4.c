// (4) Escreva o método k_str que retorna todas as k strings, em que k é menor que o tamanho da string original. Se sua string for "abc" e k for igual a 2, seu código deve imprimir na tela as substrings "aa", "ba", "ca", "ab", "bb", "cb", "ac", "bc" e "cc". Se sua string for "abc" e k for igual a 1, seu código deve imprimir na tela as substrings "a", "b", "c". O protótipo dessa função é o seguinte: void k_str(char *str, int k). DICA: USE RECURSÃO PARA RESOLVER ESSE PROBLEMA!!!

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void k_str_aux(char *str, int k, int tamanho, int posicao, char *resposta) {
    if (posicao == k) {
        resposta[posicao] = '\0';
        printf("%s\n", resposta);
        return;
    }
    for (int i = 0; str[i]; i++) {
        resposta[posicao] = str[i];
        k_str_aux(str, k, tamanho, posicao + 1, resposta);
    }
}

void k_str(char *str, int k) {
    int tamanho = strlen(str);
    char resposta[k + 1];
    int posicao = 0;
    k_str_aux(str, k, tamanho, posicao, resposta);
}

int main(void) {
    printf("Substrings de Tamanho k\n");

    char *string = malloc(1024 * sizeof(char));
    printf("Insira a string: ");
    scanf("%s", string);
    string = realloc(string, strlen(string) + 1);

    int k;
    printf("Insira o tamanho das substrings: ");
    scanf("%d", &k);
    if (k < 1) {
        printf("O tamanho das substrings deve ser pelo menos 1.");
        return 0;
    }

    k_str(string, k);

    free(string);
    return 0;
}