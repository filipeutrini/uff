/*
(Q1) Desenvolva um procedimento que receba o nome de um arquivo texto e retire deste texto palavras consecutivas repetidas. O seu programa deve retornar, no arquivo de saída, informado como parâmetro dessa função, a resposta desta questão. Por exemplo, se o conteúdo de um arquivo texto for: "Isto e um texto texto repetido repetido repetido . Com as repeticoes repeticoes fica fica sem sem sentido . Sem elas elas elas melhora melhora um um pouco .", a saída do seu programa será um arquivo com o seguinte texto: "Isto e um texto repetido . Com as repeticoes fica sem sentido . Sem elas melhora um um pouco ." - void RetRepet(char *ArqEnt, char *ArqSaida).
*/

#include <stdio.h>
#include <string.h>

void RetRepet(char *ArqEnt, char *ArqSaida) {
    FILE *entrada = fopen(ArqEnt, "r");
    if (entrada == NULL) {
        printf("Ocorreu um erro na leitura do arquivo.");
        return;
    }
    char palavra[256], anterior[256] = "";

    FILE *saida = fopen(ArqSaida, "w");
    if (!saida) {
        printf("Ocorreu um erro com o arquivo de escrita.");
        return;
    }

    while (fscanf(entrada, "%s", palavra) == 1) {
        if((strlen(anterior) == 0) || (strcmp(anterior, palavra)) ) {
            fprintf(saida, "%s ", palavra);
        }
        strcpy(anterior, palavra);
    }
}

int main(int argc, char** argv) {
    if (argc != 3) {
        printf("Erro. A entrada deve ser no formato: <exec> <arq_entrada> <arq_saida>. \n");
        return 1;
    }

    char* arq_entrada = argv[1];
    char* arq_saida = argv[2];

    RetRepet(arq_entrada, arq_saida);
    
    return 0;
}