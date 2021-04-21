# -- coding: utf-8 --
def getAreaFromPoints(valores):  # Função que irá calcular a área com base em uma lista de vértices
    d1, d2, i = 0, 0, 0  # Inicia as variáveis de cálculo diagonal 1 e 2, e o índice
    for i in range(2):  # Executa o código 2 vezes (não entendi porque não seria o tamanho do vetor menos um, mas o URI só aceitou assim)
        # Multiplica o primeiro valor da linha pelo segundo valor da próxima linha
        d1 += valores[i][0] * valores[i + 1][1]
        d2 += valores[i][1] * valores[i + 1][0]

    result = d1 - d2  # Calcula a diferença entre os resultados
    if result < 0:  # Multiplica o resultado por menos um se for negativo, efetivamente transformando-o em positivo.
        result = result * -1

    # Multiplica o resultado por 0.5 (divide por dois) como diz o método para cálculo de área via vértices
    result = result * 0.5
    return result  # Retorna o resultado


terreno1 = []  # Inicia os vetores em que os valores de ambos terrenos serão armazenados
terreno2 = []
for j in range(4):  # Executa quatro vezes (pois são quatro vértices)
    # Recebe a entrada, transforma-a em lista de entradas com split, a função map transforma em inteiro ambos valores,
    # a função list transforma-a em lista, para que possa ser acessada via [índice] e por fim,
    # os valores são adicionados ao final da lista deste terreno.
    terreno1.append(list(map(int, input().split())))
for k in range(4):
    # Executa o mesmo código que acima, mas para o segundo terreno.
    terreno2.append(list(map(int, input().split())))

# Executa a função que calcula a área para cada terreno, e armazena o resultado nas variáveis resultado1 e resultado2
resultado1 = getAreaFromPoints(terreno1)  # Terreno 1
resultado2 = getAreaFromPoints(terreno2)  # Terreno 2

# Imprime o resultado final
if resultado1 > resultado2:
    print("terreno A")  # Se o terreno A for maior que o B, imprime o terreno A
else:  # Se não, o terreno A é igual ou menor que B, logo imprime terreno B (o enunciado especifica terreno B em caso de empate).
    print("terreno B")
