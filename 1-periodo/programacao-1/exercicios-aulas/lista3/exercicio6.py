'''
Usando o método de Newton-Raphson, escreva um programa que aproxima a raiz quadrada de um número x.
O método de Newton-Raphson é um método iterativo utilizado para calcular as raízes de uma equação f(x) = 0. Partindo de uma estimativa inicial da raiz dada por x₀, o método gera uma nova aproximação xᵢ₊₁ calculando a intersecção da reta passando por xᵢ com inclinação dada por f'(xᵢ).
A fórmula da iteração de Newton é:
xᵢ₊₁ = xᵢ - f(xᵢ)/f'(xᵢ)
Expressando √x como f(x) = x² - a = 0, aplique a fórmula de iteração de Newton repetidamente até que xᵢ₊₁ - xᵢ seja menor que uma tolerância epsilon.
'''

if __name__ == "__main__":
    print("Método de Newton-Raphson")

    a = float(input("Insira o número que deseja tirar a raíz: "))
    e = float(input("Insira o erro tolerado na raíz: "))

    x = 1

    while True:
        x2 = (1/2) * (x + (a/x))
        if abs(x-x2) < e:
            break
        else:
            x = x2

    print(f"√{a} = {x2}")