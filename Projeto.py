
#  ******************************************************
#  ***********         Projeto 2            *************
#  ***********  Fundamentos da Programacao  *************
#  ***********                              *************
#  ***********      Carolina Carreira       *************
#  ***********           87641              *************
#  ******************************************************


# *******************************************************
#      Tipo POSICAO
# *******************************************************


# CONSTRUTOR
# faz_pos: natural x natural --> posicao

# faz_pos (l,c) Cria tipo posicao
def faz_pos(l,c):
    if not isinstance (l, int) or l != abs (l):
        raise ('ERRO: ValueError faz_pos')

    if not isinstance (c, int) or c != abs (c):
        raise ValueError ('faz_pos: argumentos errados')

    return (l,c,)


# SELETOR
# linha_pos|colunas_pos: posicao --> natural

# Seleciona a linha ou coluna da posicao
def linha_pos (p):    
    return p[0]

def coluna_pos (p):    
    return p[1]


# RECONHECEDORES
# e_pos: universal --> Boolean

# e_pos (arg) Reconhece o ipo posicao, este tem de ser tuplo constituido por dois elementos positivos, e inteiros
def e_pos (arg):
    return isinstance(arg, tuple) and len (arg) == 2 or isinstance (linha_pos (arg), int) and not linha_pos (arg) != abs(linha_pos (arg)) and isinstance (coluna_pos (arg), int) and not coluna_pos (arg) != abs(coluna_pos (arg))
        
    
# TESTES
# pos_iguais: posicao x posicao --> Boolean

# pos_iguais (p1, p2) recebe dois argumentos do tipo posicao, p1 e p2, e devolve
# True caso os argumentos correspondam a mesma posicao da chave
def pos_iguais (p1, p2):
    return linha_pos (p1) == linha_pos (p2) and coluna_pos (p1) == coluna_pos (p2)




# *******************************************************
# Tipo CHAVE
# *******************************************************




# CONSTRUTORES
# gera_chave_linhas: L x str --> chave

# gera_chave_linhas(l, mgc) recebe dois argumentos, l e mgc, correspondentes 
# a um tuplo de 25 letras e a cadeira de caracteres mgc e devolve a chave gerada
# usando a disposicao por linhas
def gera_chave_linhas (letras, mgc):
    
    # funcao auxiliar que verifica a validade dos argumentos L e mgc
    if not verificacao_letras_mgc (letras, mgc):      
        raise ValueError ('gera_chave_linhas: argumentos errados')              
    
    # Transforma em lista para poder ser manipulado
    letras = list(letras)                  
    
    r = []
    
    # Verifica cada letras dentro de mgc
    for i in range (len( mgc)):
        
        # Testa se o caracter nao esta ja em r e se esta em letras
        if not mgc[i] in r and mgc[i] in letras:
            
            # Se sim, junta-o a r
            r += [mgc[i]]
            
            # Remove de letras esse caracter de mgc
            letras.remove (mgc[i])
    
    # Concatena r com o que resta em letras (todos os caracteres nao presentes em mgc)
    r = r + letras
    
           # Corta em listas de listas 
    return [r[0:5],r[5:10],r[10:15],r[15:20],r[20:25]]



# AUXILIAR (funcao gera_chave_linhas e
#           funcao gera_chave_espiral
# verificacao_letras_mgc: L + mgc --> boolean

# verificacao_letras_mgc (L, mgc) verifica a validade dos argumentos letras, L, e mgc
# Para ser True o argumento L tem de ser um tuplo com 25 letras maiusculas como 
# elementos unicos e o argumento mgc tem de ser uma string de letras maiusculas
def verificacao_letras_mgc (L, mgc):
    
    # Testa de se L  e tuplo, tem tamanho 25, e se mgc e string de caracteres maiusculos
    if not isinstance (L, tuple) or len(L) != 25 or not isinstance (mgc, str) or mgc != mgc.upper ():
        return False
    
    for i in range (len (L)):
        for j in range (i+1, len(L)):
            
            # Testa se elementos sao todos diferentes e maiusculos
            if L[i] == L[j] or L[i].upper == L[i] :
                return False
    return True
            




# gera_chave_espiral: L x str x {'r','c'} x pos --> chave

# gera_chave_espiral (l; mgc; s; pos) recebe 4 argumentos, l corresponde a 
# um tuplo de 25 letras e mgc a mensagem de geracao de chave, e devolve a
# chave gerada usando a disposicao em espiral no sentido indicado pelo parametro
# s ('r' sentido dos ponteiros do rel0gio e 'c' sentido contrario),
# comecando na posicao indicada pelo parametro pos.
def gera_chave_espiral (letras, mgc, s, p):
    
    # Para os argumentos serem validos p tem de ser do tipo posicao, s tem de ser str
    # de tamanho 1, e verificacao_letras_mgc tem de ser verdadeiro
    if not e_pos (p) or not isinstance (s, str) or len(s) != 1 or not verificacao_letras_mgc (letras, mgc):
        
        raise ValueError ('gera_chave_espiral: argumentos errados')
    
    # Transforma em lista para poder ser manipulado
    letras = list(letras)                  
    
    r = []
    
    # Verifica cada caracter dentro de mgc
    for i in range (len( mgc)):
        
        # Testa se o caracter nao esta ja em r e se esta em letras
        if not mgc[i] in r and mgc[i] in letras:
            
            # Se sim, junta-o a r
            r += [mgc[i]]
            
            # Remove de letras esse caracter de mgc
            letras.remove (mgc[i])
            
    # soma o que restou nas letras (os caracteres nao presentes em mgc)
    r += letras  

    # Ordena em espiral segundo a posicao
    r = ordenar (r, p)

    if s == 'c':
        
        # se for contra os ponteiros a matriz tem de ser transposta
        r = transpor (r, p)
    
    # corta
    r = [r[0:5],r[5:10],r[10:15],r[15:20],r[20:25]]    
    
    return r



# AUXILIAR (gera_chave_linhas)
# ordenar: lista + posicao --> lista 

# ordenar (l,p) recebe uma lista, e uma posicao inicial a partir da qual ordena a lista em espiral
# no sentido dos ponteiros do relogio
def ordenar (l, p):                 

    # ordem e o dicionario com as posicoes em espiral 
    dic_posicoes = {(0,0) : dic00, (0,4) : dic04, (4,0): dic40, (4,4): dic44}
    ordem = dic_posicoes [p]

    resp = []
    
    for i in range (0, 25):
        
        # Coloca em resp a respetiva letra de l agora de forma ondenada  
        resp += [ l [ordem[i]] ]
    
    return resp

# Dicionarios de posicoes (Def ordenar)
dic00 = {0:0, 1:1, 2:2, 3:3, 4:4, 5:15, 6:16, 7:17, 8:18, 9:5, 10:14, 11:23, 12:24, 13:19, 14:6, 15:13, 16:22, 17:21, 18:20, 19:7, 20:12, 21:11, 22:10, 23:9, 24:8}
dic04 = {0:12, 1:13, 2:14, 3:15, 4:0, 5:11, 6:22, 7:23, 8:16, 9:1, 10:10, 11:21, 12:24, 13:17, 14:2, 15:9 , 16:20, 17:19, 18:18, 19:3, 20:8, 21:7, 22:6, 23:5, 24:4}
dic44 = {0:8, 1:9 , 2:10, 3:11, 4:12, 5:7, 6:20, 7:21, 8:22, 9:13, 10:6, 11:19, 12:24, 13:23, 14:14, 15:5, 16:18, 17:17, 18:16, 19:15, 20:4, 21:3, 22:2, 23:1, 24:0}
dic40 = {0:4, 1:5, 2:6, 3:7, 4:8, 5:3 , 6:18, 7:19, 8:20, 9:9 , 10:2 , 11:17, 12:24, 13:21, 14:10, 15:1 , 16:16, 17:23, 18:22, 19:11, 20:0 , 21:15, 22:14, 23:13,24:12}





# Funcao auxiliar (gera_chave_linhas)
# transpor: lista + posicao --> lista

# transpor (l,p) recebe uma lista a transpor, e uma posicao inicial para saber como transpor.
# Se for 0,0 or 4,4 a transposicao e uma reflexao em relacao a diagonal principal
# Se for 0,4 ou 4,0 esta e uma reflexao em relacao a diagonal secundaria
def transpor (l, p):
    d = []

    # Matriz de replexao em relacao a diagonal principal
    dic = transposicao_impar

    # Se for 4,4 ou 0,0 reflexao em relacao a diagonal pricipal
    if linha_pos (p) == coluna_pos (p):
        dic = transposicao_par
    
    # Caso contrario e em relacao a diagonal secundaria
    else:
        dic = transposicao_impar

    for i in range (25):
        # Ordena os elementos de l segundo o dicionario escolhido
        d += [ l [dic[i]] ]

    return d


# Dicionario de transposicao (def transpor)
transposicao_par = {0:0, 1:5, 2:10, 3:15, 4:20, 5:1, 6:6, 7:11, 8:16, 9:21, 10:2, 11:7, 12:12, 13:17, 14:22, 15:3, 16:8, 17:13, 18:18, 19:23, 20:4, 21:9, 22:14, 23:19, 24:24}
transposicao_impar = {0:24, 1:19, 2:14, 3:9, 4:4, 5:23, 6:18, 7:13, 8:8, 9:3, 10:22, 11:17, 12:12, 13:7, 14:2, 15:21, 16:16,	17:11, 18:6, 19:1, 20:20, 21:15, 22:10, 23:5, 24:0}




# SELETOR
# ref_chave: chave x posicao --> letra

# ref_chave(c; p) recebe como argumentos a chave c e a posicao p e devolve a
# letra que esta em c na posicao p
def ref_chave (c, pos):

    return c[linha_pos (pos)] [coluna_pos(pos)]



# MODIFICADOR
# muda_chave: chave x posicao x letra --> chave

# muda_chave(c; p; l) recebe como argumentos a chave c, a posicao p e a letra l
# e devolve a chave c com a letra l na posicao p
def muda_chave (c,p,l):

    c[ linha_pos (p)][coluna_pos (p)] = l
    return c


# RECONHECEDORES
# e_chave: arg --> Boolean

# e_chave(arg): devolve True se o argumento arg for do tipo chave e Falso caso contrario
def e_chave (arg):
    ''' para ser do tipo chave tem de ser uma lista constituida por 5 listas cada uma com 5 elementos
    que sejam letras maiusculas unicas'''
    if len (arg) != 5 or not isinstance (arg, list):
        return False

    for a in arg:
        
        # Testa tipo, tamanho, e se nao ha letras repetidas em cada lista dentro da lista
        if not isinstance (arg, list) or len(a) != 5 or len (set (a)) != len (a): 
            return False
        for b in a:
            
            # Testa de algum elemento e uma letra minuscula
            if not ( 64 < ord(b) < 91):
                return False
    else:
        return True


# TRANSFORMADORES
# string_chave: chave --> str

# string_chave(c) devolve uma cadeia de caracteres que uma vez impressa apresenta
# as letras de c dispostas numa tabela 5 x 5
def string_chave (chave):
    c = ''
    for linha in chave:
        
        # Coloca espacos entra as letras
        for celula in linha:
            c = c + celula + ' '
            
        # Coloca no fim de cada linha paragrafo
        c += '\n'
    return c    



# **********************************************************
#           FUNCOES A DESEMVOLVER
# **********************************************************


# diagramas: str --> str

# digramas (mens) recebe como argumento uma cadeia de caracteres 
# correspondente a uma mensagem, mens, e devolve a cadeia de caracteres
# correspondente aos digramas transformados de mens sem espacos
def digramas (mens):
    mensg = ''
    
    for i in range (len(mens)-1, -1, -1):
        
        # Retira espacos
        if mens [i] != ' ':
            mensg = mens[i] + mensg
    
    for i in range (0, len(mensg)-1, 2):
        
        # Coloca X se existirem digitos iguais
        if mensg[i] == mensg [i+1]:
            mensg = mensg[:i+1] + 'X' + mensg[i+1:]  
    
    # Testa para ver se ha numeros par de caracteres
    if len (mensg) % 2 != 0:
        
        # Se nao houver acrescenta X no fim
        mensg += 'X'    
    
    return mensg



# figura: digrm + chave --> fig + pos1 + pos2

# figura(digrm, chave) recebe dois argumentos, digrm, uma cadeia de
# caracteres de comprimento 2, e chave, e devolve um tuplo de 3 elementos
# da forma (fig, pos1, pos2) em que:
#     - fig e a figura determinada pelas letras de digrm, 'l', 'c' ou 'r' (linha, coluna ou
#       rectangulo).
#     - pos1 e pos2 sao as posicoes ocupadas na chave pela primeira e segunda letras de
#       digrm, respectivamente.
def figura (digrm, chave):
    t = ()
    
    # Ciclo para determinar posicao de uma letra na chave
    for a in digrm:
        
        # cada lista dentro da lista
        for i in range (0,5):
            
            for j in range (0,5):
                
                # Verifica se o digito e igual ao digito da posicao i,j da chave
                if a ==  ref_chave (chave, faz_pos (i,j)):
                    
                    # Encontra posicao do digito e acumula
                    t += (faz_pos(i,j),)  
     
    # Testa se estao na mesma linha               
    if linha_pos(t[0]) == linha_pos(t[1]):
        return ('l',) + t
    
    # Testa de estao na mesma coluna
    if coluna_pos (t[0]) == coluna_pos (t[1]):
        return ('c',) + t
    
    # Se estao em retangulo
    else:
        return ('r',) + t     
    


# codifica_l: posicao + posicao + {-1,1} --> posicao + posicao

# codifica_l (pos1, pos2, inc) recebe tres argumentos, pos1, pos2, 
# consistindo nas posicoes das letras de um digrama na mesma linha de uma
# chave, e o inteiro inc, que podera ser 1 (encriptar) ou -1 (desencriptar). 
# Devolve um tuplo de 2 posicoes (pos1_cod, pos2_cod) que correspondem as
# posicoes das letras do digrama encriptado/desencriptado.
def codifica_l (pos1, pos2, inc):
    c = ()
    # Acede a cada posicao dada
    for posicao in (pos1,pos2):
        
        # Testa se a coluna e 1, 2, 3
        if coluna_pos (posicao) != 4 and coluna_pos (posicao) != 0 :
            
            # se sim, retorna a mesma posicao com a coluna alterada ( coluna + 1 
            # se for encriptacao, coluna - 1 se for desencriptacao)
            c += ( faz_pos ( linha_pos (posicao) , coluna_pos (posicao) + inc ), )
            
        # Testa se e encriptacao
        elif inc == 1:
            
            # se sim e se a posicao tiver 4 na coluna entao volta a ficar com 0
            # se esta tiver 0 atualiza a coluna com 1 (0+1)
            c += (faz_pos ( linha_pos (posicao) , 0),) if coluna_pos (posicao) == 4 else (faz_pos ( linha_pos (posicao) , 1),)


        # Desemcriptacao
        else:
            # Se a posicao tiver 4 na coluna fica com 3 (4-1)
            # Se tiver 0 fica com 4
            c += (faz_pos ( linha_pos (posicao) , 3),) if coluna_pos (posicao) == 4 else (faz_pos ( linha_pos (posicao) , 4),)
            
    return c
    



# codifica_l: posicao + posicao + {-1,1} --> posicao + posicao

# codifica_l (pos1, pos2, inc) recebe tres argumentos, pos1, pos2, 
# consistindo nas posicoes das letras de um digrama na mesma coluna de uma
# chave, e o inteiro inc, que podera ser 1 (encriptao) ou -1 (desencriptar). 
# Devolve um tuplo de 2 posicoes (pos1_cod, pos2_cod) que correspondem as
# posicoes das letras do digrama encriptado/desencriptado.
def codifica_c (pos1, pos2, inc):
    c = ()
    
    # Acede a cada posicao dada
    for posicao in (pos1,pos2):
        
        # Testa se a linha e 1, 2, 3
        if linha_pos (posicao) != 4 and linha_pos (posicao) != 0 :
            
            # se sim, retorna a mesma posicao com a linha alterada ( linha + 1 
            # se for encriptacao, linha - 1 se for desencriptacao)            
            c += ( faz_pos ( linha_pos (posicao) + inc, coluna_pos (posicao)), )
            
        # Testa se e encriptacao    
        elif inc == 1:
            
            # se sim e se a posicao tiver 4 na linha entao volta a ficar com 0
            # se esta tiver 0, atualiza a linha com 1 (0+1)            
            c += (faz_pos ( 0 , coluna_pos (posicao)),) if linha_pos (posicao) == 4 else (faz_pos ( 1 , coluna_pos (posicao)),)
       
       # Desemcriptacao
        else:
            
            # Se a posicao tiver 4 na linha fica com 4-1 = 3
            # Se tiver 0 fica volta ao 4            
            c += (faz_pos ( 3 , coluna_pos (posicao)),) if linha_pos (posicao) == 4 else (faz_pos ( 4, coluna_pos (posicao)),)
    
    return c



# codifica_r: posicao + posicao --> posicao + posicao

# codifica_r (pos1, pos2) recebe dois argumentos, pos1, pos2, consistindo nas
# posicoes das letras de um digrama numa chave. Estas posicoes encontra-se 
# em linhas e colunas diferentes. 
# A funcao devolve (pos1_cod, pos2_cod) que correspondem as posicoes das letras
# do digrama encriptado/desencriptado
def codifica_r (pos1, pos2):
    
    # Retorna duas posicoes com as colunas trocadas entre si
    return  faz_pos(linha_pos(pos1), coluna_pos(pos2),) , faz_pos(linha_pos(pos2), coluna_pos(pos1))




# codifica_digrama: cad + chave + {1,-1} --> cad

# codifica_digrama ( diagrm, c, inc) recebe tres argumentos, digrm, um digrama,
# chave, uma chave, e o inteiro inc, que podera ser 1(encriptacao) ou 
# -1 (desencriptacao).
# A funcao devolve o digrama correspondente a encriptacao/desencriptacao de digrm
# usando a chave.
def codifica_digrama ( diagrm, c, inc):
    # Funcao figura que devolve as posicoes dos caracteres no diagrama
    # e a sua posicao relativa (na mesma linha, coluna, ou em rectangulo)
    coordenadas = figura (diagrm, c)

    # Verifica o ultimo elemento retornado por figura se e 'l'
    if coordenadas [0] == 'l':
        
        # Chama a funcao codifica_l que devolve duas posicoes (encriptadas ou 
        # desencriptadas) que estejam na mesma linha
        diretriz = codifica_l ( coordenadas [1],  coordenadas [2], inc)
        
        # Devolve as dois caracteres correspondentes as duas posicoes
        return ref_chave( c, faz_pos (linha_pos(diretriz [0]), coluna_pos(diretriz [0]))) + ref_chave ( c, faz_pos (linha_pos(diretriz [1]), coluna_pos(diretriz [1])))
    
    # Se ultimo elemento retornado por figura e 'c'
    if coordenadas [0] == 'c':
        
        # Chama a funcao codifica_c que devolve duas posicoes (encriptadas ou 
        # desencriptadas) que estejam na mesma coluna        
        diretriz = codifica_c ( coordenadas [1],  coordenadas [2], inc)

        # Devolve as dois caracteres correspondentes as duas posicoes
        return ref_chave ( c, faz_pos (linha_pos(diretriz [0]), coluna_pos(diretriz [0]))) + ref_chave (c, faz_pos (linha_pos(diretriz [1]), coluna_pos(diretriz [1])))        

    else:
        # Chama a funcao codifica_c que devolve duas posicoes (encriptadas ou 
        # desencriptadas) que nao estejam na mesma linha ou coluna (em rectangulo)          
        diretriz = codifica_r ( coordenadas [1],  coordenadas [2])
        
        
        # Devolve as dois caracteres correspondentes as duas posicoes
        return ref_chave ( c,faz_pos(linha_pos(diretriz [0]),  coluna_pos(diretriz [0]))) + ref_chave (c, faz_pos (linha_pos(diretriz [1]), coluna_pos(diretriz [1])))
    
    

# codifica: mens + chave + {1,-1} --> mens

# codifica (mens, chave, inc) recebe tres argumentos, mens, uma mensagem,
# chave, uma chave, e o inteiro inc, que podera ser 1(encriptacao) ou -1
# (desencriptacao). 
# A funcao devolve a mensagem correspondente a encriptacao/desencriptacao de mens
# usando a chave.
def codifica (mens, chave, inc):
    
    # Chama a funcao diagramas que devolve uma str igual a mens, sem espacos
    # e sem caracteres repetidos
    mens  = digramas (mens)
    r = ''
    
    # Codifica os caracteres dois a dois
    for i in range (0, len(mens)-1, 2):
        
        # Chama codifica_digrama que devolve dois caracteres codificados
        r += codifica_digrama (mens[i:i+2], chave, inc) 
        
    return r



l = ('A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

