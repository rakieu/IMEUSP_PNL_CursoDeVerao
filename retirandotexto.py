from PNL.corpus import corpus
classes_corretas = [entrada[1] for entrada in corpus]
classes_previstas = []

texto = [entrada[0] for entrada in corpus]

def tokenize(texto):
    indesejados = ['.', ',', ';', ':', '!', '?']
    partes = texto.split()
    cont = 0
    while cont < len(partes):
        if partes[cont][-1] in indesejados:
            partes[cont] = partes[cont][0: len(partes[cont])-1]
        cont += 1
    return partes

def filtra_dicionario(freq, freq_min):
    freq_filtrado = {}
    for key in freq:
        if freq[key] > freq_min:
            freq_filtrado[key] = freq[key]
    return freq_filtrado(freq)

def conta_palavras(texto, freq_min):
    tokens = tokenize(texto)
    freq = {}
    for token in tokens:
        if token not in freq:
            freq[token] = 1
        else:
            freq[token] += 1
    return filtra_dicionario(freq, freq_min)

print(conta_palavras(texto, freq_min))
