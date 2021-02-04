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




#codigo

lista_de_palavras = str(textoAves)

for palavra in lista_de_palavras:
    if palavra not in frequenciaAves:
        frequenciaAves[palavra] = 1
    else:
        frequenciaAves[palavra] = frequenciaAves[palavra] + 1
print(frequenciaAves)




p_computadores = ['máquina', 'informações', 'processamento']

texto = [entrada[0] for entrada in corpus]

for f in texto:
    frases = f.split()
    for palavras in frases:
        if palavras in p_computadores:
            classes_previstas.append(1)
            break
        else:
            classes_previstas.append(0)

#print(f)
#print('\n', 'C_PREV', classes_previstas, '\n')








#CODIGO REAL

def dicAves(textoAves):
lista_de_palavras = textoAves.split()

for palavra in lista_de_palavras:
    if palavra not in frequenciasAves:
        frequenciasAves[palavra] = 1
    else:
        frequenciasAves[palavra] = frequenciasAves[palavra] + 1

print('O DICIONARIO DE FREQUENCIAS PRODUZIDO FOI:\n')
print(frequenciasAves)



