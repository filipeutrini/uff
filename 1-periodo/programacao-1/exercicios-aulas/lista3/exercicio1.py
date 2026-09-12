'''
Exercício 1: Soma de uma sequência de inteiros
Escreva um programa em Python que calcule a soma de todos os inteiros em um intervalo de a a b.
'''

if __name__ == "__main__":
    print("Somatório do Intervalo")
    a = int(input("Insira um número a: "))
    b = int(input("Insira um número b: "))

    soma = 0
    for i in range(a, b+1):
        soma += i
    print(f"Soma = {soma}")