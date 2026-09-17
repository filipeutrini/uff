// (2) Dados n arquivos ordenados, gere um arquivo de saída ordenado contendo todos os elementos dos arquivos de entrada, sem usar qualquer algoritmo de ordenação. O protótipo da função é o seguinte: void ordena(char **arqs, int n, char *arq_saida).

// vou considerar os arquivos contendo números ordenados em ordem crescente.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ordena(char **arqs, int n, char *arq_saida) {
    FILE **f = malloc(n * sizeof(FILE*));
    int *valor = malloc(n * sizeof(int));
    int *ativo = malloc(n * sizeof(int));  // 0 se acabaram os dados do arquivo

    // abre todos os arquivos e lê o primeiro elemento de cada um
    for (int i = 0; i < n; i++) {
        f[i] = fopen(arqs[i], "r");
        if (f[i] && fscanf(f[i], "%d", &valor[i]) == 1) {
            ativo[i] = 1;
        } else {
            ativo[i] = 0;
        }
    }

    FILE *saida = fopen(arq_saida, "w");

    while (1) {
        int menor_arq = -1;
        int menor = 999999999;

        // encontra qual arquivo tem o menor valor (ou igual ao atual)
        for (int i = 0; i < n; i++) {
            if (ativo[i] && valor[i] <= menor) {
                menor = valor[i];
                menor_arq = i;
            }
        }

        // quando acabam todos os dados, ele para
        if (menor_arq == -1) break;

        fprintf(saida, "%d\n", menor);

        if (fscanf(f[menor_arq], "%d", &valor[menor_arq]) != 1) {
            ativo[menor_arq] = 0; // quando chega ao fim do arquivo, ele deixa o arquivo inativo
        }
    }

    for (int i = 0; i < n; i++) {
        if (f[i]) fclose(f[i]);
    }
    fclose(saida);
    free(f);
    free(valor);
    free(ativo);
}

int main(int argc, char** argv) {
    printf("Arquivos Ordenados\n");
    int tam = argc - 2;
    char **entradas = &argv[1];
    char *saida = argv[argc - 1];

    if(argc < 3) {
        printf("A entrada deve ser no formato: <exec> <arq_entrada1> <arq_entrada2> <...> <arq_saida>\n");
        return 1;
    }

    ordena(entradas, tam, saida);
    return 0;
}