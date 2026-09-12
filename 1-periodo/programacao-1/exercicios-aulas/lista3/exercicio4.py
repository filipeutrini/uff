'''
Exercício 4: Cálculo do número de dígitos de um inteiro
Escreva um programa que determine o número de dígitos de um inteiro n.
'''

if __name__ == "__main__":
    print("Número de Digitos de um Número")

    n = int(input("Insira um número inteiro: "))
    n = abs(n)

    digitos = 0
    num = n
    while num > 0:
        digitos += 1
        num = num // 10

    if digitos != 1:
        print(f"O número {n} possui {digitos} digitos.")
    else:
        print(f"O número {n} possui 1 digito.")