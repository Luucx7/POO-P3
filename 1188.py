# -*- coding: utf-8 -*-
caso = input()  # Recebe se o caso será soma (S) ou média (M)

soma = float(0)  # Define soma com o valor inicial de zero, declarado como ponto flutuante
matriz = []  # Cria um vazio, que irá armazenar todos os valores

for i in range(12):  # Executa um laço 12 vezes, sendo referente a linha da matriz
    matriz.append([])  # Adiciona um vetor vazio na posição i (linha)
    for j in range(12):  # Executa outro laço dentro de cada laço, referente a coluna da matriz
        matriz[i].append(float(input()))  # Adiciona o valor a matriz na posição referente

maior = 7  # Inicia as variáveis maior e menor, que receberão inicialmente as posições das colunas em que estão os valores desejados.
menor = 5  # A variável maior será somada a cada iteração, e a menor será subtraída em cada (ambos por 1).

for k in range(7, 12):  # Como queremos saber a parte inferior, esta está contida a partir da linha 7, logo itera-se a partir dela.
    for l in range(menor, maior):  # Itera entre os valores entre menor e maior
        soma += matriz[k][l]  # Adiciona o valor encontrado à variável soma
    maior += 1  # Diminui e soma um as variáveis menor e maior, para controlar os valores necessários
    menor -= 1

if caso == "S":  # Caso seja uma operação de soma, imprime o valor da soma bruto
    print("%.1f" % soma)
else:  # Se não, será uma operação de média. Como a parte inferior sempre possúi 30 valores, divide-se a soma dos valores por 30 e imprime para obter a média.
    print("%.1f" % (soma / 30))
