'''
13) Implemente um programa em Python que receba um inteiro e verifique se ele é um palíndromo, isto é, se a sua sequência de dígitos se iguala aos dígitos na ordem inversa.
'''

if __name__ == "__main__":
    num = int(input("Insira um número inteiro: "))

    original = abs(num)
    invertido = 0
    temp = original

    while temp > 0:
        digito = temp % 10
        invertido = invertido * 10 + digito
        temp //= 10

    if original == invertido:
        print(f"{num} é um palíndromo.")
    else:
        print(f"{num} não é um palíndromo.")