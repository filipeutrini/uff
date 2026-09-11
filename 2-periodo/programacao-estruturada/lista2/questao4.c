/*
Q4) [Problema 1533 do URI Online Judge] John Watson, mesmo após anos trabalhando ao lado de Sherlock Holmes, nunca conseguiu entender como ele consegue descobrir quem é o assassino com tanta facilidade. Em uma certa noite, porém, Sherlock bebeu mais do que devia e acabou contando o segredo a John. “Elementar, meu caro Watson”, disse Sherlock Holmes. “Nunca é o mais suspeito, mas sim o segundo mais suspeito”. Após descobrir o segredo, John decidiu resolver um crime por conta própria, só para testar se aquilo fazia sentido ou se era apenas conversa de bêbado. Dada uma lista com N inteiros, representando o quanto cada pessoa é suspeita, ajude John Watson a decidir quem é o assassino, de acordo com o método citado.
Haverá diversos casos de teste. Cada caso de teste inicia com um inteiro N (2 ≤ N ≤ 1000), representando o número de suspeitos. Em seguida haverá N inteiros distintos, onde o i-ésimo inteiro, para todo 1 ≤ i ≤ N, representa o quão suspeita a i-ésima pessoa é, de acordo com a classificação dada por John Watson. Seja V o valor do i-ésimo inteiro, 1 ≤ V ≤ 10000. O último caso de teste é indicado quando N = 0, o qual não deverá ser processado. Para cada caso de teste imprima uma linha, contendo um inteiro, representando o indice do assassino, de acordo com o método citado.
*/

#include <stdio.h>

int main(void) {
    printf("Método do Sherlock Holmes\n");
    while (1) {
        int N;
        scanf("%d", &N);
        if (N == 0) break;

        int maior = -1;
        int segundo_maior = -1;
        int id_maior = 0;
        int id_segundo = 0;

        for (int i = 1; i <= N; i++) {
            int suspeita;
            scanf("%d", &suspeita);

            if (suspeita > maior) {
                segundo_maior = maior;
                id_segundo = id_maior;

                maior = suspeita;
                id_maior = i;
            } 
            else if (suspeita > segundo_maior) {
                segundo_maior = suspeita;
                id_segundo = i;
            }
        }

        printf("%d\n", id_segundo);
    }

    return 0;
}
