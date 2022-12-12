from xml.dom.minidom import parse
from dicionario import criar_dicionario_global, soma_pontuacao_das_paginas, dicionario_ordenado_da_palavra_selecionada
from busca_e_ordenacao import criar_busca, mostrar_palavras_ordenadas

docs = parse('verbetesWikipedia.xml')
raiz = docs.firstChild

pages = raiz.getElementsByTagName("page")

tamanho_min_palavra = 4
tamanho_cache = 1000
valor_titulo = 10
valor_texto = 1


#pre processamento
print("Criando Dicionario para as paginas:")
dicionario_global, todas_palavras = criar_dicionario_global(pages, valor_titulo, valor_texto,tamanho_min_palavra)


#Todas as palavras que existe no texto
print("Criando um dicionario de busca para todas as palavras")
cache = criar_busca(dicionario_global, todas_palavras,tamanho_cache)


while True:

    palavra_buscada = input("Buscar palavra:")
    
    if palavra_buscada == '0':
        break
    
    palavra_buscada_split = palavra_buscada.split(' ')
    vetor_dicionario = []
    
    for palavra in palavra_buscada_split:
        vetor_dicionario.append(dicionario_ordenado_da_palavra_selecionada(cache, palavra, dicionario_global))
    
    if len(vetor_dicionario) == 1:
        mostrar_palavras_ordenadas(vetor_dicionario[0])
        continue
    
    dicionario_composto = soma_pontuacao_das_paginas(vetor_dicionario)
    
    mostrar_palavras_ordenadas(dicionario_composto)
    
        