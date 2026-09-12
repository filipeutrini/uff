'''
Exercício 2: Computador simplificado
Faça um programa que execute instruções de 16 em uma cpu hipotética com um registrador acumulador acc e dois registrador auxiliares ax e bx. Nas instruções de 16 bits, os 8 bits mais significativos representam o tipo de operação e os demais bits codificam valores de 8 bits que podem ser dados (ou endereços de memória a serem usados no futuro)
O programa deve rodar em um laço (loop), lendo instruções do teclado até que o usuário entre com a instrução 0. A cada instrução executada o computador deve imprimir o estado dos registradores e a instrução que acabou de ser executada.

Exemplos de instrução:
0b0000000100001111 mov acc, 00001111
0b0000001000001111 mov ax, 00001111
0b0000001100000011 mov bx, 00000011
0b0000010000000011 add acc, 00000011

Exemplo de execução:
Estado da cpu
acc= 0
ax= 0
bx = 0
Digite uma instrucao em binario - tecle 0 para terminar: 0b0000000100001111
Instrucao: (dec)271, (bin) 0000000100001111
opcode: (dec)1, (bin)00000001
operand: (dec)15, (bin)00001111
Estado da cpu
acc= 15
ax= 0
bx= 0
Digite uma instrucao em binario - tecle 0 para terminar: 0
'''

if __name__ == "__main__":
    acc = 0
    ax = 0
    bx = 0

    while True:
        print("Estado da CPU")
        print(f"acc= {acc}")
        print(f"ax= {ax}")
        print(f"bx= {bx}")

        instrucao = input("Digite uma instrucao em binario - tecle 0 para terminar: ").strip()

        if instrucao == "0":
            break

        instrucao = int(instrucao, 2)

        opcode = (instrucao >> 8) & 0xFF
        operand = instrucao & 0xFF

        instrucao_bin = f"{instrucao:016b}"
        opcode_bin = f"{opcode:08b}"
        operand_bin = f"{operand:08b}"

        match opcode:
            case 1:  # mov acc, operand
                acc = operand
            case 2:  # mov ax, operand
                ax = operand
            case 3:  # mov bx, operand
                bx = operand
            case 4:  # add acc, operand
                acc += operand
            case 5:  # add acc, ax
                acc += ax
            case 6:  # add acc, bx
                acc += bx
            case _:
                print("Instrução inválida.")

        print(f"Instrucao: (dec){instrucao} , (bin) {instrucao_bin}")
        print(f"opcode: (dec){opcode}, (bin){opcode_bin}")
        print(f"operand: (dec){operand},(bin){operand_bin}")