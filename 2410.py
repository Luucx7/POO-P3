# -*- coding: utf-8 -*-
quantia = int(input())  # Recebe a quantia de valores e transforma em inteiro

alunos = {}  # Cria um dicionário vazio, que irá armazenar o código do aluno e quantas vezes aparece

for i in range(quantia):  # Executa a leitura quantia vezes
    value = int(input())  # Recebe um valor e transforma em inteiro
    if alunos.__contains__(value):  # Verifica se a lista de alunos contém tal valor de aluno
        quantia = alunos.get(value)  # Caso sim, retorna o valor do aluno, e soma um, por fim atribuindo ao dicionário novamente
        alunos[value] = quantia + 1
    else:  # Se não existe, adiciona ao dicionário
        alunos[value] = 1

# Já que o dicionário não aceitará valores repetidos, o seu tamanho será igual ao de valores únicos de alunos.
print(len(alunos))  # Imprime o tamanho do dicionário de alunos
