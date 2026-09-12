'''
1) Escreva um programa em Python que leia os dados de uma turma. Em cada interação são lidos a matrícula, o nome e a nota de cada aluno. A leitura se encerra quando uma matrícula zero for digitada (flag). Calcule os seguintes dados:
    a) a média das notas dos alunos
    b) o total de alunos aprovados
    c) o total de alunos reprovados
    d) o total de alunos em VS
    e) O desvio padrão das notas.
'''

if __name__ == "__main__":
    print("Análise da Turma")
    aprovados = reprovados = vs = soma_notas = soma_quadrados = total_alunos = 0

    while True:
        matricula = int(input("Digite a matrícula (0 para encerrar): "))
        if matricula == 0:
            break
            
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))

        soma_notas += nota
        soma_quadrados += nota**2
        total_alunos += 1
        
        # Classificação do aluno
        if nota >= 6.0:
            aprovados += 1
        elif nota >= 4.0:
            vs += 1
        else:
            reprovados += 1

    if total_alunos > 0:
        media = soma_notas / total_alunos
        
        variancia = (soma_quadrados / total_alunos) - (media ** 2)
        
        desvio_padrao = variancia**(1/2)
        
        print(f"Média das notas: {media:.2f}")
        print(f"Total de alunos aprovados: {aprovados}")
        print(f"Total de alunos reprovados: {reprovados}")
        print(f"Total de alunos em VS: {vs}")
        print(f"Desvio padrão das notas: {desvio_padrao:.2f}")
    else:
        print("Nenhum aluno foi cadastrado.")