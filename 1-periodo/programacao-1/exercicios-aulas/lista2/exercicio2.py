'''
Exercício 2: Ordenação de 3 números
Dados três números inteiros armazenados nas variáveis a, b e c, escreva um programa que troque seus valores de forma que ao imprimir a, b e c, nesta sequência, os valores estejam em ordem crescente.
'''

if __name__ == "__main__":
    print("Ordenação de 3 Números")
    a = int(input("Insira o número a: "))
    b = int(input("Insira o número b: "))
    c = int(input("Insira o número c: "))

    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > c:
        a, c = c, a

    print(a, b, c)