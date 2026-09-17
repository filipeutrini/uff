// (1) Inserir o elemento (x - 1) antes e o elemento (x + 1) depois de cada ocorrência de x em uma string de resposta. Se sua string original for formada pelos elementos {'1','3','1','5','1','\0'}, e se x for igual a '1', sua string de resposta será {'0','1','2','3','0','1','2','5','0','1','2','\0'}. O protótipo dessa função é o seguinte: char* ins_antes_depois_x(char* str, char x).

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* ins_antes_depois_x(char *str, char x) {
    char *resp = malloc((strlen(str) + 1) * sizeof(char));
    int pos = 0;
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == x) {
            resp[pos] = str[i] - 1;
            pos++;
            resp[pos] = str[i];
            pos++;
            resp[pos] = str[i] + 1;
            pos++;
        } else {
            resp[pos] = str[i];
            pos++;
        }
    }
    resp[pos] = '\0';

    return resp;
}

int main(void) {
    char string[6] = {'1', '3', '1', '5', '1', '\0'};
    char x = '1';

    printf("%s\n", string);

    char *nova = ins_antes_depois_x(string, x);

    printf("%s", nova);

    return 0;
}