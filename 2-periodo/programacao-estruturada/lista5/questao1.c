/*
Q1) Dada uma matriz quadrada de dimensão 9, com valores de 1 a 9 em suas posições, escreva um programa que verifique se esta matriz é uma solução válida para o Sudoku (isto é, uma solução é válida no Sudoku se cada linha, cada coluna e cada bloco contém os números de 1 a 9 somente uma vez).
*/

#include <stdio.h>
#include <stdlib.h>

int eh_sudoku(int** tabuleiro) {
    for (int i = 0; i < 9; i++) {
        int linha[9] = {0}; // conta quais números estão na linha (0 não está e 1 está)
        int coluna[9] = {0}; // conta quais números estão na coluna
        int bloco[9] = {0}; // conta quais números estão no bloco

        for (int j = 0; j < 9; j++) {
            int num_linha = tabuleiro[i][j];
            if ((num_linha < 1) || (num_linha > 9)) return 0;

            int num_coluna = tabuleiro[j][i];
            if ((num_coluna < 1) || (num_coluna > 9)) return 0;
            
            // i vai ser o número do bloco e j vai ser cada posição dentro do bloco i
            int bi = 3 * (i / 3) + (j / 3);
            int bj = 3 * (i % 3) + (j % 3);
            int num_bloco = tabuleiro[bi][bj];
            if ((num_bloco < 1) || (num_bloco > 9)) return 0;

            if (linha[num_linha - 1]++) return 0; // confere se o número está na linha e aumenta o contador daquele número
            if (coluna[num_coluna - 1]++) return 0;
            if (bloco[num_bloco - 1]++) return 0;
        }
    }

    return 1;
}

int main(void) {
    printf("Verificador de Tabuleiro de Sudoku\n");
    int** tab_sudoku = (int**) malloc(9 * sizeof(int*));
    for (int i = 0; i < 9; i++) {
        tab_sudoku[i] = (int*) malloc(9 * sizeof(int));
    }

    for (int i = 0; i < 9; i++) {
        printf("Insira a %dª linha do tabuleiro de sudoku: ", i + 1);
        for (int j = 0; j < 9; j++) {
            scanf("%d", &tab_sudoku[i][j]);
        }
    }

    if (eh_sudoku(tab_sudoku)) {
        printf("O tabuleiro é valido.");
    } else {
        printf("O tabuleiro não é válido.");
    }

    for (int i = 0; i < 9; i++) {
        free(tab_sudoku[i]);
    }
    free(tab_sudoku);
}