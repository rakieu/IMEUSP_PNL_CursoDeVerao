# Programa que extrai as frequencias de aparicao das palavras em um texto,
# alocando-as em um dicionario.

texto = '''rosas são vermelhas
violetas são azuis
não são não
violetas são roxas'''

frequencias = {}

lista_de_palavras = texto.split()

for palavra in lista_de_palavras:
    if palavra not in frequencias:
        frequencias[palavra] = 1
    else:
        frequencias[palavra] = frequencias[palavra] + 1

print('O DICIONARIO DE FREQUENCIAS PRODUZIDO FOI:\n')
print(frequencias)