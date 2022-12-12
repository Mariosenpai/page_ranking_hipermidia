from tqdm import tqdm
from getNodeText import getNodeText
from busca_e_ordenacao import buscar_palavra

def verificar_se_existe_no_dicionario(valor, dicionario, palavra,tamanho_min_palavra):
    
    if len(palavra) >= tamanho_min_palavra:
        
        #Verifica se a palavra ja existe no dicionario
        if palavra in dicionario:
            valor_antigo = dicionario[palavra]
            dicionario.update({palavra : valor_antigo + valor})
        else:
            #Se ele nn existe entao criar uma palavra
            dicionario[palavra] = valor  
            
    return dicionario


def criar_dicionario_global(pages, valor_titulo, valor_texto,tamanho_min_palavra):
    
    dicionario_global = {}
    todas_palavras = []
    
    for page in tqdm(pages):
            
        dicionario_palavras = {}

        
        titulo = getNodeText(page.getElementsByTagName("title")[0])
        titulo = titulo.lower()
        titulo_split = titulo.split(' ')
        for palavra_titulo in titulo_split:
            dicionario_palavras = verificar_se_existe_no_dicionario(valor_titulo, dicionario_palavras, palavra_titulo, tamanho_min_palavra)
            todas_palavras.append(palavra_titulo)


        texto = getNodeText(page.getElementsByTagName("text")[0])
        texto = texto.lower()
        texto_split = texto.split(' ')
        for palavra_texto in texto_split:
            verificar_se_existe_no_dicionario(valor_texto, dicionario_palavras, palavra_texto,tamanho_min_palavra)
            todas_palavras.append(palavra_texto)
                
        dicionario_global[titulo] = dicionario_palavras 
        
    return dicionario_global , todas_palavras



def dicionario_ordenado_da_palavra_selecionada(cache,palavra_buscada, dicionario_global):
    
    remove_cache = True
    for palavra_salva in cache:
        
        if palavra_salva == palavra_buscada:
            
            dic_busca = buscar_palavra(dicionario_global , palavra_buscada )
            remove_cache = False
            

    if remove_cache:
        
        dic_busca = buscar_palavra(dicionario_global, palavra_buscada)
        
        if len(dic_busca) == 0:
            print("Palavra não encontrada")
            return None
        
        cache.popitem()
        cache[palavra_buscada] = dic_busca;
        
        
    return dic_busca;

def soma_pontuacao_das_paginas(vetor_dicionario,):
    dic_final = {}
    primeira_interacao = True
    for dicionario in vetor_dicionario:

        for chave in dicionario:
            
            if primeira_interacao:
                dic_final[chave] = dicionario[chave]
            else:
                dic_final.setdefault(chave , 0 )
                
                valor_final = int(dicionario[chave]) + int(dic_final[chave])
                dic_final.update({chave: valor_final })
        
        primeira_interacao = False    
          
    return dic_final   