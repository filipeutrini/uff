'''
Exercício 1: Cálculo de inclinação de uma rampa
Escreva um programa em Python que verifique se uma rampa atende às especificações adequadas sugeridas pela NBR 9050.
A inclinação da rampa i, dada a altura do desnível a, e o comrpimento da rampa projetada c é dada por i = (a/c)*100.
    a) Cálcule a inclinação da rampa.
    b) Verifique se a inclinação satisfaz os requisitos de inclinação máxima para pedestres e veículos.
    Pedestres: Inclinação máxima de 8%
    Veículos: Inclinação máxima de 20%
'''

if __name__ == "__main__":
    print("Verificador de Inclinação de Rampa")

    a = float(input("Insira a altura do desnível: "))
    c = float(input("Insira o comprimento da rampa: "))

    i = abs((a/c)*100)

    print(f"Inclinação: {i}")

    if i > 20:
        print("A inclinação da rampa não é adequada")
    elif i <= 8:
        print("A inclinação da rampa é adequada para veículos e pedestres.")
    else:
        print("A inclinação da rampa é adequada para veículos.")