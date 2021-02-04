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
    return freq_filtrado

def conta_palavras(texto, freq_min):
    tokens = tokenize(texto)
    freq = {}
    for token in tokens:
        if token not in freq:
            freq[token] = 1
        else:
            freq[token] += 1
    return filtra_dicionario(freq, freq_min)

print(conta_palavras('Os pássaros, pássaros no céu, não se se lembram do chão.', 1))