import random
from random import randint
from random import choice

def calc_soma (calc_num):
    '''calc_soma = string -> int
       calc_soma (calc_num) recebe uma string, inverte a ordem dos algarismos, multiplica os numeros de ordem impar por dois e para os que tenham valor superior a nove, subtrai nove. Posteriormente soma todos os valores de ordem impar e par e divide por dez. Caso o resto da divisao por dez seja zero, devolve True, caso contrario devolve False.'''
    
    calc_num = (calc_num)[::-1]
    i = 0
    somafinal = 0
    num_elementos = len(calc_num)
    
    while i < num_elementos:  
        if i % 2 == 0:
            soma1 = eval (calc_num [i]) * 2
            if soma1 > 9:
                soma1 = soma1 - 9
            somafinal = somafinal + soma1    
        else:
            somafinal = somafinal + eval (calc_num [i])
        i = i + 1
    return somafinal

def luhn_verifica (calc_num):
    # Falta comentário

    somafinal = calc_soma (calc_num [:-1]) + eval (calc_num [-1])
    
    if somafinal % 10 == 0:
        return True
    else:
        return False
    
def comeca_por (cad1, cad2):
    '''comeca_por: str x str -> logic
       comeca_por recebe duas cadeias de caracteres e devolve o valor logico True se cad1 comecar por cad2, caso contrario devolve False.'''
    
    i = 0
    compr_cad2 = len(cad2)
    
    if len (cad2) <= len (cad1):
        while i < compr_cad2:
            if cad2 [i] in cad1 [i]:
                i = i + 1
            else:
                return False           
        return True
    else:    
        return False
    
def comeca_por_um (cad, t_cads):
    '''comeca_por_um: str x tuple -> logic
    comeca_por_um recebe duas cadeias de caracteres e devolve o valor logico True se a cad1 comecar por t_cads, caso contrario devolve False.'''      
            
    i = 0 
    compr_t_cads = len (t_cads)

    while i < compr_t_cads:       
        if t_cads[i] == cad [:len(t_cads[i])]:
            return True
        i = i + 1
    return False
    
def valida_iin (num_cc):
    '''valida_iin: str -> str
    valida_iin recebe uma string contendo o numero de cartao de credito e retorna o nome correspondente da Rede Emissora.'''
    
    if comeca_por_um (num_cc, ('34', '37')) and len (num_cc) == 15:  
        return 'American Express'
    elif comeca_por_um (num_cc, ('309', '36', '38', '39')) and len (num_cc) == 14:
        return 'Diners Club International'
    elif comeca_por_um (num_cc, ('69')) and len (num_cc) == 16:
        return 'Discover Card'
    elif comeca_por_um (num_cc, ('5018', '5020', '5038')) and (len (num_cc) == 13 or len (num_cc) == 19):
        return 'Maestro'
    elif comeca_por_um (num_cc, ('50', '51', '52', '53', '54', '19')) and len (num_cc) == 16:
        return 'Master Card'
    elif comeca_por_um (num_cc, ('4026', '426', '4405', '4508')) and len (num_cc) == 16:
        return 'Visa Electron'
    elif comeca_por_um (num_cc, ('4024', '4532', '4556')) and (len (num_cc) == 13 or len (num_cc) == 16):
        return 'Visa'
    else:
        return ''
    
def categoria (entid):
    '''categoria: str - > str
       categoria recebe uma string contendo o numero de cartao de credito e devolve a categoria da entidade correspondente ao primeiro caracter.'''
    
    entid = eval(entid[0])
  
    if entid == 1:
        return 'Companhias aereas'
    elif entid == 2:
        return 'Companhias aereas e outras tarefas futuras da industria'
    elif entid == 3:
        return 'Viagens e entretenimento e bancario / financeiro'
    elif entid == 4:
        return 'Servicos bancarios e financeiros'
    elif entid == 5:
        return 'Servicos bancarios e financeiros'
    elif entid == 6:
        return 'Merchandising e bancario / financeiro'
    elif entid == 7:
        return 'Petroleo e outras atribuicoes futuras da industria'
    elif entid == 8:
        return 'Saude, telecomunicacoes e outras atribuicoes futuras da industria'
    elif entid == 9:
        return 'Atribuicao nacional'

def verifica_cc (num_cc):
    '''verifica_cc: str - > tuple
       verifica_cc recebe uma string contendo o numero de cartao de credito e devolve um tuplo com 2 elementos, um com a categoria do cartao e outro com a entidade emissora. Em caso contrario, devolve uma string a dizer cartao invalido.'''    
    
    num_cc = str (num_cc)
    
    if luhn_verifica (num_cc) == True:
        if valida_iin (num_cc) == '':
            return 'cartao invalido'
        else:
            return (categoria (num_cc), valida_iin (num_cc))
    else:
        return 'cartao invalido'
    
# Gerar um cartao de credito --------------------------------------------------

def digito_verificacao (num_menos_um):
    '''digito_verificacao: str - > str
       digito_verificacao recebe uma string contendo um numero de cartao de credito e devolve uma string contendo o numero de verificacao.'''
    
    soma = calc_soma (num_menos_um)
    resto = soma % 10

    if resto == 0:
        return str(0)
    else:
        resto = 10 - (soma % 10)
    return str (resto)

def gera_num_cc(emissora):
    '''gera_num_cc: str->str
       gera_num_cc recebe uma string contendo a abreviatura da emissora e devolve   
       um numero do cartao valido gerado correspondente'''
    
    def gerador (length):
        '''gerador:: str-> str
        gerador e uma funcao auxiliar que recebe uma string vinda da funcao 
        gera_num_cc e devolve uma string contendo os numeros aleatorios a ser 
        usados pelo cartao'''
       
        num =''
        while len(num) < length:
            num = num +str(random.randint(0,9))
        return num
    
    if emissora == 'AE':
        primeiros = random.choice(('34','37')) 
        length = 15 - 1 - len(primeiros)
        intermedios = str(gerador(length))
        verificacao = str(digito_verificacao(primeiros + intermedios))
        return str(str(primeiros)+str(intermedios)+str(verificacao))
    elif emissora == 'DCI':
        primeiros = random.choice(('309', '36', '38', '39')) 
        length = 14 - 1 - len(primeiros)
        intermedios = str(gerador(length))
        verificacao = str(digito_verificacao(primeiros + intermedios))
        return str(str(primeiros)+str(intermedios)+str(verificacao))
    elif emissora == 'DC':
        primeiros = ('65') 
        length = 16 - 1 - len(primeiros)
        intermedios = str(gerador(length))
        verificacao = str(digito_verificacao(primeiros + intermedios))
        return str(str(primeiros)+str(intermedios)+str(verificacao))    
    elif emissora == 'M':
        primeiros = random.choice(('5018','5020','5038'))
        length = random.choice((13 - 1 - len(primeiros), 19 - 1 - len(primeiros)))
        intermedios = str(gerador(length))
        verificacao = str(digito_verificacao(primeiros + intermedios))
        return str(str(primeiros)+str(intermedios)+str(verificacao))    
    elif emissora == 'MC':
        primeiros = random.choice(('50','51','52','53','54','19'))
        length = (16 - 1 - len(primeiros))
        intermedios = str(gerador(length))
        verificacao = str(digito_verificacao(primeiros + intermedios))
        return str(str(primeiros)+str(intermedios)+str(verificacao))  
    elif emissora == 'V':
        primeiros = random.choice(('4024','4532','4556'))
        length = random.choice(((16 - 1 - len(primeiros), 13 - 1 - len(primeiros))))
        intermedios = str(gerador(length))
        verificacao = str(digito_verificacao(primeiros + intermedios))
        return str(str(primeiros)+str(intermedios)+str(verificacao))
    elif emissora == 'VE':
        primeiros = random.choice(('4026','426','4405','4508'))
        length = 16 - 1 - len(primeiros)
        intermedios = str(gerador(length))
        verificacao = str(digito_verificacao(primeiros + intermedios))
    return str(str(primeiros)+str(intermedios)+str(verificacao))    