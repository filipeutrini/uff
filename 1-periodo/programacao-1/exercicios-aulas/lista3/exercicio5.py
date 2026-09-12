'''
Exercício 5: Conversão de um número em base decimal para base binária
    a) Escreva um programa que leia um número decimal e gere sua representação binária
    b) Faça o mesmo exercício utilizando apenas o tipo inteiro e operações aritméticas (sem auxílio de strings nem arrays)
'''

'''
# a)
if __name__ == "__main__":
    print("Conversor de Decimal para Binário")

    n = int(input("Insira um número decimal: "))

    print(f"Representação em binário: {bin(n)[2:]}")
'''

# b)
if __name__ == "__main__":
    print("Conversor de Decimal para Binário")

    n = int(input("Insira um número decimal: "))

    binario = 0
    mult = 1

    while n > 0:
        binario = (n % 2) * mult + binario
        n = n // 2
        mult *= 10

    print(f"Representação em binário: {binario}")