/*
(Q3) Escreva uma função que receba, como entrada, uma cadeia de caracteres s e um inteiro n, e, em seguida, retire o "prefixo" da cadeia s de tamanho n (isto é, retire os n primeiros caracteres). Se a cadeia não tiver pelo menos n caracteres, deve ser impressa a mensagem "erro". Por exemplo, se s = "abcdefghi" e n = 3, então a cadeia "defghi" deve ser impressa; com a mesma cadeia s e n = 17, deve ser impresso "erro". O protótipo desta função é o seguinte: void retira_inicio_n (char *str, int n).
*/

#include <stdio.h>
#include <string.h>

void retira_inicio_n(char* str, int n) {
    if (strlen(str) < n) printf("Erro.");
    else if (strlen(str) != n) {
        for(int i = n; i < strlen(str); i++) {
            printf("%c", str[i]);
        }
    }
}

int main(void) {
    printf("Retirar do Início da String\n");

    char s[100];
    printf("Insira uma string: ");
    scanf(" %s", &s);

    int n;
    printf("Número de caracteres que deseja remover do inicio: ");
    scanf("%d", &n);

    retira_inicio_n(s, n);

    return 0;
}