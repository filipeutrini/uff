'''
12) Escreva um program em Python que implemente uma calculadora capaz de realizar as quatro operações aritméticas +,-,*,/. O usuário digita a operação desejada na forma de um caractere ('+','-','*' ou '/') seguido pelo par de operandos a e b e o resultado desejado é impresso no console. O programa deve executar repetidamente até que o usuário digite 's' no lugar de uma operação válida.
'''

if __name__ == "__main__":
    while True:
        op = input("Insira a operação (+, -, *, /) ou 's' para sair: ").strip()
        
        if op == 's':
            break
            
        if op in ('+', '-', '*', '/'):
            a = float(input("Insira o primeiro operando: "))
            b = float(input("Insira o segundo operando: "))
            
            if op == '+':
                res = a + b
            elif op == '-':
                res = a - b
            elif op == '*':
                res = a * b
            elif op == '/':
                if b == 0:
                    print("Erro: divisão por zero.")
                    continue
                res = a / b
                
            print(f"Resultado: {a} {op} {b} = {res}\n")
        else:
            print("Operação inválida.\n")