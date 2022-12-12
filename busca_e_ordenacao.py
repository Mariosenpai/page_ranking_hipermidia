
from tqdm import tqdm

def buscar_palavra(dicionario_global, palavra_buscada):
    
    dicionario_busca = {}
    for page in dicionario_global:
        dicionario = dicionario_global[page]
        #Dicionario das paginas

        #Adiciona o valor daquela palavra ao dicionario com a chave igual ao nome da pagina
        if palavra_buscada in dicionario:
            dicionario_busca[page] = dicionario[palavra_buscada]
            
    return dicionario_busca
                    
def criar_busca(dicionario_global, todas_palavras, tamanho_cache):
    
    dicionario_busca_por_palavra = {}
    cache = {}
    for palavra_buscada in tqdm(todas_palavras):

        #Todas as paginas 
        if len(cache) <= tamanho_cache:
            # print("tamanha = ", len(cache))
            
            dicionario_busca = buscar_palavra(dicionario_global, palavra_buscada)
                    
            dicionario_busca_por_palavra[palavra_buscada] = dicionario_busca
            cache = dicionario_busca_por_palavra
        elif len(cache) > tamanho_cache:
            return cache


def mostrar_palavras_ordenadas(dicionario_busca ):
    dic_busca_ord = orderna_dicionario(dicionario_busca)
    for chave in dic_busca_ord:
        print(chave ,":", dic_busca_ord[chave])
        
def orderna_dicionario(dic):
    ord_dic = {}
    for item in sorted(dic, key = dic.get):
        ord_dic[item] = dic[item]
    return ord_dic