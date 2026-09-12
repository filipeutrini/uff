'''
5) Escreva um programa que leia um número e determine sua representação binária que deve ser armazenada em um único inteiro.
'''

if __name__ == "__main__":
    n = int(input("Insira um número inteiro: "))

    binario = 0
    mult = 1

    while n > 0:
        binario = (n % 2) * mult + binario
        n = n // 2
        mult *= 10

    print(f"Representação em binário: {binario}")