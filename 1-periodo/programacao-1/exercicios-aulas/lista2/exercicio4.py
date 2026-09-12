'''
Exercício 4: Análise de uma instrução em código binário
    a) Escreva um programa que leia um número binário de 16 bits que representa uma instrução. Ao ler o número binário como uma string, utilize a função de conversão int configurada para base 2.
    b) Extraia o opcode (código da instrução) dos 8 bits mais significativos e o operando, que se encontra nos 8 bits menos significativos. Utilize os operadores para manipulação bit-a-bit & (and), ^ (or), ~ (not), >> (right shift), << (left shift), se necessário.
'''

if __name__ == "__main__":
    print("Análise de Instrução")

    s = input("Insira uma instrução binária de 16 bits: ")
    num = int(s, 2)
    print(f"Equivalente decimal: {num}")

    opcode = bin(num >> 8)
    operando = bin(num & 0xFF)

    print(f"Opcode = {opcode[2:].zfill(8)}")
    print(f"Operando = {operando[2:].zfill(8)}")