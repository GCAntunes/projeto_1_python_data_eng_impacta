texto = "Olá  mundo  isso é  um  exemplo de  texto"
fragmentos_dois_espacos = texto.split('  ')
fragmentos_palavras = [frag.split(' ') for frag in fragmentos_dois_espacos]
fragmentos_letras = [[list(palavra) for palavra in frag] for frag in fragmentos_palavras]
print(fragmentos_palavras,fragmentos_dois_espacos,fragmentos_letras)