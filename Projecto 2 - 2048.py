from random import choice

################################################################################
##                                                                            ##
##                         ###########################                        ##
##                         # TAD Coordenada (4 val.) #                        ##
##                         ###########################                        ##
##                                                                            ## 
################################################################################

def cria_coordenada (l, c):
    '''cria_coordenada: inteiro x inteiro -> coordenada
       cria_coordenada (l, c) recebe dois argumentos (do tipo inteiro e entre 1 e 4) sendo o primeiro deles correspondente ao numero da linha e o segundo referente ao numero da coluna, e devolve um elemento do tipo coordenada correspondente a posicao (l,c).'''
    
    if (isinstance(l, int) and 0 < l <= 4) and (isinstance(c, int) and 0 < c <=4):
        return (l, c)
    
    raise ValueError ('cria_coordenada: argumentos invalidos')

def coordenada_linha (coordenada):
    ''' coordenada_linha: coordenada -> inteiro
        coordenada_linha (coordenada) recebe uma coordenada e da-nos o respectivo valor do numero da linha.'''
    
    return coordenada [0]

def coordenada_coluna (coordenada):
    ''' coordenada_coluna: coordenada -> inteiro
        coordenada_coluna (coordenada) recebe uma coordenada e da-nos o respectivo valor do numero da coluna.'''
    
    return coordenada [1]

def e_coordenada (argumento):
    ''' e_coordenada: universal -> logico
        e_coordenada (argumento) recebe um argumento e vai verificar se este e uma coordenada ou nao. Se for uma coordenada devolve True, caso contrario devolve False.'''
    
    if isinstance (argumento, tuple) == True and \
       len(argumento) == 2 and \
       isinstance (argumento [0], int) == True and isinstance (argumento [1], int) == True and \
       (0 < coordenada_linha (argumento) <= 4 and 0 < coordenada_coluna (argumento) <= 4):
        return True
    
    return False

def coordenadas_iguais (coordenada_1, coordenada_2):
    ''' coordenadas_iguais: coordenada x coordenada -> logico
        coordenadas_iguais (coordenada_1, coordenada_2) recebe duas coordendas e caso elas sejam iguais, ou seja, correspondem a mesma posicao do tabuleiro, devolve True, caso contrario devolve False.'''
    
    if coordenada_linha (coordenada_1) == coordenada_linha (coordenada_2) and \
       coordenada_coluna (coordenada_1) == coordenada_coluna (coordenada_2):
        return True

    return False


################################################################################
##                                                                            ##
##                         ###########################                        ##
##                         # TAD Tabuleiro (6 val.)  #                        ##
##                         ###########################                        ##
##                                                                            ## 
################################################################################


def cria_tabuleiro ():
    '''cria_tabuleiro: {} -> tabuleiro
       cria_tabuleiro () nao recebe qualquer argumento e devolve um dicionario.'''
    
    return ({(1,1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0, (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 0, 'Pontuacao': 0})

def tabuleiro_posicao (t, c):
    '''tabuleiro: tabuleiro x coordenada -> inteiro
       tabuleiro_posicao (t, c) recebe dois argumentos, um do tipo tabuleiro e outro do tipo coordenada, devolvendo um inteiro correspondente ao valor na posicao da coordenada c.'''
    
    if e_coordenada (c) == True: 
        c = (coordenada_linha(c),coordenada_coluna(c))
        return t[c]
    
    return ValueError ('tabuleiro_posicao: argumentos invalidos')

def tabuleiro_pontuacao (t):
    '''tabuleiro_pontuacao: tabuleiro -> inteiro
       tabuleiro_pontuacao (t) recebe um argumento do tipo tabuleiro e devolve a pontuacao atual para o tabuleiro.'''
    
    return t ['Pontuacao']

def tabuleiro_posicoes_vazias (t):
    '''tabuleiro_posicao: tabuleiro -> lista
       tabuleiro_posicao (t) recebe um argumento do tipo tabuleiro e devolve uma lista de todas as coordenadas que se encontram vazias.'''
    
    l = 1    
    lista = []
    
    while l <= 4:
        c = 1
        while c <= 4:    
            if tabuleiro_posicao(t,cria_coordenada(l,c)) == 0:
                lista.append(cria_coordenada(l,c))
            
            c = c + 1 
        l = l + 1
   
    return lista

def tabuleiro_preenche_posicao (t, c, v):
    '''tabuleiro_preenche_posicao : tabuleiro x coordenada x inteiro -> tabuleiro
       tabuleiro_preenche_posicao (t, c, v) recebe um argumento do tipo tabuleiro, um do tipo coordenada e outro do tipo inteiro devolvendo um do tipo tabuleiro, mas modificado. Esta funcao ao receber um inteiro referente a posicao c, vai modificar o valor da respetiva posicao no tabuleiro.'''
     
    if e_coordenada (c) == False or \
       isinstance (v, int) == False:
        raise ValueError ('tabuleiro_preenche_posicao: argumentos invalidos')
    
    else:
        c = (coordenada_linha(c),coordenada_coluna(c))
        t[c] = v
        return t

def tabuleiro_actualiza_pontuacao (t, v):
    '''tabuleiro_actualiza_pontuacao: tabuleiro x inteiro -> tabuleiro
       tabuleiro_actualiza_pontuacao (t, v) recebe dois argumentos, um do tipo tabuleiro e um inteiro. Devolve o tabuleiro com a pontuacao actualizada pelo valor de v.'''
    
    if v > 0  and (v % 4 == 0) and isinstance(v,int):
        t ['Pontuacao'] += v
        return t
    
    raise ValueError ('tabuleiro_actualiza_pontuacao: argumentos invalidos')        
    
def tabuleiro_reduz (t, d):
    '''tabuleiro_reduz: tabuleiro x string -> tabuleiro
       tabuleiro_reduz (t, d) recebe dois argumentos, um do tipo tabuleiro e uma string que vai modifica-lo de acordo com as regras do jogo (movimenta as pecas do tabuleiro nas direccoes Norte, Sul, Este, Oeste).'''
    
    if d in ('W'):
        # Merge whitespace
        for _ in range(4):
            for i in range(1,5):
                for c in range(1,4):
                    if t[i, c+0] == 0 and t[i, c+1] != 0:
                        t[i, c] = t[i, c+1]
                        t[i, c+1] = 0
 
        # Merge neighbors
        for i in range(1,5):
            for c in range(1,4):
                if t[i, c+0] == t[i, c+1] and t[i, c] != 0:
                    t[i, c] *= 2
                    t[i, c+1] = 0
                    t['Pontuacao'] = tabuleiro_pontuacao(tabuleiro_actualiza_pontuacao(t,tabuleiro_posicao(t,cria_coordenada(i,c))))
                elif t[i,c+0] == 0 and t[i,c+1] == 0:
                    t[i,c] = t[i,c+1]
                    t[i,c+1] = 0                
 
        # Merge whitespace
        for _ in range(4):
            for i in range(1,5):
                for c in range(1,4):
                    if t[i+0, c] == 0 and t[i, c+1] != 0:
                        t[i+0, c] = t[i, c+1]
                        t[i, c+1] = 0
              
        return t
        
    if d in ('E'):
        for _ in range(4):
            for i in range(1,5):
                for c in reversed(range(2,5)):
                    if t[i, c+0] == 0 and t[i, c-1] != 0:
                        t[i, c] = t[i, c-1]
                        t[i, c-1] = 0
                    
        
        # Merge neighbors   
        for i in range(1,5):
            for c in reversed(range(2,5)):
                if t[i, c+0] == t[i, c-1] and t[i, c] != 0:
                    t[i, c] *= 2
                    t[i, c-1] = 0
                    t['Pontuacao'] = tabuleiro_pontuacao(tabuleiro_actualiza_pontuacao(t,tabuleiro_posicao(t,cria_coordenada(i,c))))
                elif t[i,c+0] == 0 and t[i,c-1] == 0:
                    t[i,c] = t[i,c-1]
                    t[i,c-1] = 0
   
        # Merge whitespace
        for _ in range(4):
            for i in range(1,5):
                for c in range(2,5):
                    if t[i+0, c] == 0 and t[i, c-1] != 0:
                        t[i+0, c] = t[i, c-1]
                        t[i, c-1] = 0
                    elif t[i,c] == 0 and t[i,c-1] == 0:
                        t[i,c] = t[i,c-1]
                        t[i,c-1] = 0
        return t

        
    if d in ('S'):
        # Merge whitespace
        for _ in range(4):
            for i in reversed(range(2,5)):
                for c in range(1,5):
                    if t[i, c+0] == 0 and t[i-1, c] != 0:
                        t[i, c] = t[i-1, c]
                        t[i-1, c] = 0
     
        # Merge neighbors
        for i in reversed(range(2,5)):
            for c in range(1,5):
                if t[i, c+0] == t[i-1, c] and t[i, c] != 0:
                    t[i, c] *= 2
                    t[i-1, c] = 0
                    t['Pontuacao'] = tabuleiro_pontuacao(tabuleiro_actualiza_pontuacao(t,tabuleiro_posicao(t,cria_coordenada(i,c))))
                elif t[i,c+0] == 0 and t[i-1,c] != 0:
                    t[i,c] = t[i-1,c]
                    t[i,c] = 0                    
                    
    
        # Merge whitespace
        for _ in range(4):
            for i in reversed(range(2,5)):
                for c in range(1,5):
                    if t[i+0, c] == 0 and t[i-1, c] != 0:
                        t[i+0, c] = t[i-1, c]
                        t[i-1, c] = 0    
        
            return t

    if d in ('N'):
        # Merge whitespace    # ultima coluna nao soma os valores para cima
        for _ in range(4):
            for i in range(1,4):
                for c in range(1,5):
                    if t[i, c+0] == 0 and t[i+1, c] != 0:
                        t[i, c] = t[i+1, c]
                        t[i+1, c] = 0
       
        # Merge neighbors
        for i in range(1,4):
            for c in range(1,5):
                if t[i, c+0] == t[i+1, c] and t[i, c] != 0:
                    t[i, c] *= 2
                    t[i+1, c] = 0
                    t['Pontuacao'] = tabuleiro_pontuacao(tabuleiro_actualiza_pontuacao(t,tabuleiro_posicao(t,cria_coordenada(i,c))))
                elif t[i,c+0] == 0 and t[i,c] == 0:
                    t[i,c] = t[i,c]
                    t[i,c] = 0                  
             
        # Merge whitespace
        for _ in range(4):
            for i in range(1,4):
                for c in range(1,5):
                    if t[i+0, c] == 0 and t[i+1, c] != 0:
                        t[i+0, c] = t[i+1, c]
                        t[i+1, c] = 0  
        return t
    
    else:
        raise ValueError('tabuleiro_reduz: argumentos invalidos')        

def e_tabuleiro (argumento):
    ''' e_tabuleiro: universal -> logico
        e_tabuleiro (argumento) recebe um argumento e vai verificar se este e um tabuleiro ou nao. Se for um tabuleiro devolve True, caso contrario devolve False.'''
    
    for c in range (1,5):
        for l in range(1,5):
            if ((not isinstance(argumento,dict) or not isinstance(tabuleiro_posicao(argumento,cria_coordenada(c,l)),int)) or (tabuleiro_posicao(argumento,cria_coordenada(c,l)) < 0)):
                return False
    return (len(argumento) == 17 and tabuleiro_pontuacao(argumento) >= 0 and isinstance(tabuleiro_pontuacao(argumento),int))

def tabuleiro_terminado (t):
    '''tabuleiro_terminado: tabuleiro -> logico
       tabuleiro_terminado (t) recebe um argumento do tipo tabuleiro e devolve True caso este esteja terminado, ou seja, nao hajam mais possiveis movimentos. Caso contrario devolve False.'''
   
    x = copia_tabuleiro (t)
    for j in ('S','N','W','E'):
        if not tabuleiros_iguais(t,tabuleiro_reduz(x,j)):
            return False  
    return True

def tabuleiros_iguais (t1, t2):
    '''tabuleiros_iguais: tabuleiro x tabuleiro -> logico
       tabuleiros_iguais (t1, t2) recebe dois argumentos do tipo tabuleiro e devolve True caso os dois tabuleiros sejam iguais em termos de configuracao e pontuacao, caso contrario devolve False.'''
    
    return t1==t2
    

def escreve_tabuleiro (t):
    '''escreve_tabuleiro: tabuleiro -> {}
       escreve_tabuleiro (t) recebe um argumento do tipo tabuleiro e escreve para o ecra a representacao externa de um tabuleiro do jogo 2048.'''    
        
    if e_tabuleiro (t) == True:
        print ('[',tabuleiro_posicao(t,cria_coordenada(1,1)),']','[',tabuleiro_posicao(t,cria_coordenada(1,2)),']','[',tabuleiro_posicao(t,cria_coordenada(1,3)),']','[',tabuleiro_posicao(t,cria_coordenada(1,4)),'] \n'
               '[',tabuleiro_posicao(t,cria_coordenada(2,1)),']','[',tabuleiro_posicao(t,cria_coordenada(2,2)),']','[',tabuleiro_posicao(t,cria_coordenada(2,3)),']','[',tabuleiro_posicao(t,cria_coordenada(2,4)),'] \n'
               '[',tabuleiro_posicao(t,cria_coordenada(3,1)),']','[',tabuleiro_posicao(t,cria_coordenada(3,2)),']','[',tabuleiro_posicao(t,cria_coordenada(3,3)),']','[',tabuleiro_posicao(t,cria_coordenada(3,4)),'] \n'
               '[',tabuleiro_posicao(t,cria_coordenada(4,1)),']','[',tabuleiro_posicao(t,cria_coordenada(4,2)),']','[',tabuleiro_posicao(t,cria_coordenada(4,3)),']','[',tabuleiro_posicao(t,cria_coordenada(4,4)),'] \n'
               'Pontuacao:', tabuleiro_pontuacao(t))    
    else:
        raise ValueError ('escreve_tabuleiro: argumentos invalidos')
    
def pede_jogada ():
    '''pede_jogada: {} -> string
       pede_jogada () nao recebe qualquer argumento, simplesmente pede ao utilizador para introduzir uma direccao para a sua jogada.'''
   
    jogada = input('Introduza uma jogada (N, S, E, W): ')
    
    if jogada not in ('N' , 'S', 'E', 'W'):
        print ('Jogada invalida.')
        return pede_jogada ()
    else:
        return jogada
      
def copia_tabuleiro (t):
    
    x = t.copy()
    
    return x

def preenche_posicao_aleatoria (t):
    '''preenche_posicao_aleatoria: tabuleiro -> {}
    preenche_posicao_aleatoria (t) recebe um argumento do tipo tabuleiro e preenche uma posicao do tabuleiro que esteja vazia com os numeros 2 ou 4, de acordo com as suas probabilidades de aparecerem.'''
        
    x = random.choice (tabuleiro_posicoes_vazias(t))
    y = random.choice ((2,2,2,2,4))
    
    return tabuleiro_preenche_posicao (t, (coordenada_linha(x),coordenada_coluna(x)), y)
        
def jogo_2048 ():
    '''jogo_2048: {} -> {}
       jogo_2048 () nao recebe qualquer argumento nem devolve algo.'''      

    # Gera o tabuleiro inicial
    t = cria_tabuleiro ()
    
    for _ in range (0,2):
        preenche_posicao_aleatoria (t)  
    
    # Jogada
    escreve_tabuleiro (t)
    while tabuleiro_terminado (t) != True:
        x = copia_tabuleiro (t)
        
        tabuleiro_reduz (t, str(pede_jogada ()))
        if tabuleiros_iguais(t,x) == False:
            preenche_posicao_aleatoria (t)
        
        escreve_tabuleiro (t)