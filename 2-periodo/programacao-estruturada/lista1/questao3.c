/*
Q3) [Problema 1103 do URI Online Judge] Daniela é enfermeira em um grande hospital, e tem os horários de trabalho muito variáveis. Para piorar, ela tem sono pesado, e uma grande dificuldade para acordar com relógios despertadores. Recentemente ela ganhou de presente um relógio digital, com alarme com vários tons, e tem esperança que isso resolva o seu problema. No entanto, ela anda muito cansada e quer aproveitar cada momento de descanso. Por isso, carrega seu relógio digital despertador para todos os lugares, e sempre que tem um tempo de descanso procura dormir, programando o alarme despertador para a hora em que tem que acordar. No entanto, com tanta ansiedade para dormir, acaba tendo dificuldades para adormecer e aproveitar o descanso.
Um problema que a tem atormentado na hora de dormir é saber quantos minutos ela teria de sono se adormecesse imediatamente e acordasse somente quando o despertador tocasse. Mas ela realmente não é muito boa com números, e pediu sua ajuda para escrever um programa que, dada a hora corrente e a hora do alarme, determine o número de minutos que ela poderia dormir.
Entrada: a entrada contém vários casos de teste. Cada caso de teste é descrito em uma linha, contendo quatro números inteiros H1, M1, H2, M2, com H1:M1 representando a hora e minuto atuais, e H2:M2 representando a hora e minuto para os quais o alarme despertador foi programado (0≤H1≤23, 0≤M1≤59, 0≤H2≤23, 0≤M2 ≤59). O final da entrada é indicado por uma linha que contém apenas quatro zeros, separados por espaços em branco.
Saída: para cada caso de teste da entrada seu programa deve imprimir uma linha, cada uma contendo um número inteiro, indicando o número de minutos que Daniela tem para dormir.
*/

#include <stdio.h>

int main() {
    printf("Tempo de Sono\nInsira a hora de inicio e de fim (Formato: H1 M1 H2 M2):\n");
    while (1) {
        int h1, m1, h2, m2;
        while (1) {
            scanf("%d %d %d %d", &h1, &m1, &h2, &m2);
            if ((0 <= h1 && h1 <= 23) && (0 <= m1 && m1 <= 59) && (0 <= h2 && h2 <= 23) && (0 <= m2 && m2 <= 59)){
                break;
            }
        }

        if (h1 == 0 && m1 == 0 && h2 == 0 && m2 == 0) {
            break;
        }

        h1 *= 60;
        h2 *= 60;

        int t1, t2;
        t1 = h1+m1;
        t2 = h2+m2;
        if (t2 <= t1) {
            t2 += 1440;
        }
        
        int sono = t2 - t1;
        printf("%d\n", sono);
    }

    return 0;
}
