'''
Exercício 2: Determinar aprovação em uma disciplina
Dada a média parcial de um aluno antes da VS, determine se um aluno está aprovado, reprovado ou em VS. Um aluno está aprovado se sua média é maior ou igual a 6.0. Deve fazer Verificação Suplementar se sua média é maior ou igual a 4.0 e inferior a 6.0 e está reprovado se a nota for menor que 4.0. Alunos estão reprovados por falta se não tiverem 75% de presença.
'''

if __name__ == "__main__":
    print("Aprovação de Aluno")

    media = float(input("Insira a média do aluno (0-10): "))
    presenca = float(input("Insira a porcentagem de presença do aluno (0-100%): "))

    if presenca < 75 or media < 4:
        print("Aluno reprovado.")
    elif media < 6:
        print("Aluno ficou de VS.")
    else:
        print("Aluno aprovado.")