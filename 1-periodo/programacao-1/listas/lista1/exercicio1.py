'''
1) Escreva um programa em Python que leia duas notas nota1 e nota2 e determine a aprovação do aluno (aprovado, reprovado ou VS) em função de sua média. O aluno está aprovado se média ≥ 6, em VS se 4.0 ≤ média < 6 e reprovado se média < 4.
'''

if __name__ == "__main__":
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    if media >= 6.0:
        print("Aprovado.")
    elif media >= 4.0:
        print("VS.")
    else:
        print("Reprovado.")