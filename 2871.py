# -*- coding: utf-8 -*-
while True:  # Irá repetir o código até a exceção de fim de arquivo ser lançada
    try:
        l, c = map(int, input().split())  # Receberá os valores de tamanho da matriz e transforma em inteiros

        soma = 0  # Inicia a variável soma

        for i in range(l):  # Executa um laço para as linhas da matriz
            linha = input().split()  # Recebe os valores referentes a coluna da matriz. o split já retorna um vetor
            for j in range(c):  # Para cada valor na coluna da matriz
                soma += int(linha[j])  # Adiciona a variável soma

        sacas = soma // 60  # Divide a soma por 60 e ignora o resto (sempre retornará inteiro), o que equivale a quantia de sacas de café
        litros = soma - (sacas * 60)  # Remove o valor das sacas da variável soma, retornando os litros que sobraram (efetivamente o resto), sendo uma "operação reversa" da anterior.

        print("%.0f saca(s) e %.0f litro(s)" % (sacas, litros))  # Imprime o valor e formata na tela
    except EOFError:  # Trata o erro e quebra o laço de repetição
        break
