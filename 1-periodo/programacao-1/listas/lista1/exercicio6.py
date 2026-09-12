'''
6) Escreva um programa em Python que leia os coeficientes a, b e c de uma equação do segundo grau ax² + bx + c e imprima as sua raízes reais, caso existam.
'''
if __name__ == "__main__":
    print("Raízes de Equação do 2o Grau")
    a = float(input("Insira o coeficiente a: "))
    b = float(input("Insira o coeficiente b: "))
    c = float(input("Insira o coeficiente c: "))

    delta = b**2 - 4 * a * c

    if delta < 0:
        print("A equação não possui raiz real.")
    elif delta == 0:
        raiz = (-b) / (2 * a)
        print(f"A raiz da equação é x = {raiz}")
    else:
        raiz1 = ((-b) + delta**(1/2)) / (2 * a)
        raiz2 = ((-b) - delta**(1/2)) / (2 * a)
        print(f"As raízes da equação são x = {raiz1} e x = {raiz2}")