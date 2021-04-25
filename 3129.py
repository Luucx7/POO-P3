# -*- coding: utf-8 -*-
#
# Para contar as figurinhas, será criado um dicionário em que o número da figurinha é a chave do mesmo.
# Para cada figurinha lida, se verifica se o dicionário já possui esta mesma.
# Se sim, basta somar um ao valor armazenado.
# Se não, adiciona a mesma ao dicionário com valor referente a quantidade de um (já que será a primeira vez da mesma aparecendo)
#
# Para saber quantas figurinhas únicas existem, basta contar quantas chaves foram adicionadas ao dicionário, pois
# as figurinhas repetidas serão apenas armazenadas nos valores.
#
# Para saber quantas estão repetidas, sabe-se que são N figurinhas, e que o tamanho do dicionário é referente as figurinhas únicas,
# logo, se subtrairmos a quantia de figurinhas únicas de N, teremos a quantia de figurinhas que estão repetidas.
#

N = int(input())  # Recebe a quantia de figurinhas a serem analizadas

figurinhas = {}  # Dicionário que irá conter, respectivamente, o número da figurinha e sua quantia.

for i in range(N):  # Irá executar N vezes (para cada figurinha)
    figurinha = int(input())  # Recebe um valor de figurinha

    if figurinhas.__contains__(figurinha):  # Verifica se o dicionário já possui esta figurinha
        quantia = figurinhas[figurinha]  # Se sim, retorna quantas vezes ela apareceu
        figurinhas[figurinha] = quantia + 1  # Somará um, e armazenará de volta ao dicionário de figurinhas
    else:  # Se o dicionário não possui a figurinha
        figurinhas[figurinha] = 1  # Adiciona a figurinha ao dicionário, com valor de 1 (já que ela apareceu uma vez)

print(len(figurinhas))  # Imprime a quantia de figurinhas únicas
print((N - len(figurinhas)))  # Imprime a quantia de figurinhas repetidas
