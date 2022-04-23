import ply.lex as lex
import sys

from sqlalchemy import literal


tokens = ['LEX_T', 'YACC_T', 'LEFT', 'RIGHT', 'CARD', 'TS', 
            'CHAV_A', 'SYMBOLTABLE_T', 'NEG', 'UMINUS', 'CHAV_F', 
            'PERCENTAGEM', 'PARRETOA', 'PARRETOF', 'ASPAS', 'STAT', 'EXP', 
            'PRECEDENCE_T','PLICA', 'LITERALS_T', 'IGNORE_T', 'TOKENS_T', 
            'PALM', 'SPECIAL', 'REGEX', 'RETURN', 'ERROR'] 



literals = ['+','-','*','/', '%', '(', ')', ',', '.', '=', ':']

def t_LEX_T(t):
    r'LEX'
    t.value = str(t.value)
    return t

def t_YACC_T(t):
    r'YACC'
    t.value = str(t.value)
    return t

def t_PRECEDENCE_T(t):
    r'precedence\ *'
    t.value = str(t.value)
    return t

def t_ASPAS(t):
    r'"'
    t.value = str(t.value)
    return t

def t_PARRETOA(t):
    r'\['
    t.value = str(t.value)
    return t

def t_PARRETOF(t):
    r'\]'
    t.value = str(t.value)
    return t

def t_LEFT(t):
    r'left'
    t.value = str(t.value)
    return t

def t_RIGHT(t):
    r'right'
    t.value = str(t.value)
    return t

def t_CARD(t):
    r'\#'
    t.value = str(t.value)
    return t

def t_SYMBOLTABLE_T(t):
    r'symboltable\ *'
    t.value = str(t.value)
    return t

def t_NEG(t): #trquei o %prec por %neg para nao dar conflito com o %precedence
    r'neg\ *'
    t.value = str(t.value)
    return t

def t_UMINUS(t):
    r'UMINUS\ *'
    t.value = str(t.value)
    return t

def t_STAT(t):
    r'stat\ *'
    t.value = str(t.value)
    return t


def t_EXP(t):
    r'exp\ *'
    t.value = str(t.value)
    return t


#def t_IGUAL(t):
#    r'='
#    t.value = str(t.value)
#    return t

def t_LITERALS_T(t):
    r'literals\ *'
    t.value = str(t.value)
    return t

def t_IGNORE_T(t):
    r'ignore\ *'
    t.value = str(t.value)
    return t

def t_TOKENS_T(t):
    r'tokens\ *'
    t.value = str(t.value)
    return t

def t_PLICA(t): 
    r"'"
    t.value = str(t.value)
    return t

def t_PERCENTAGEM(t): 
    r"%"
    t.value = str(t.value)
    return t

def t_PALM(t): #PALM -> palavra maiuscula
    r'[A-Z]+'
    t.value = str(t.value)
    return t

def t_SPECIAL(t):  #\t \n ou espaço
    r'(\\[tn]|\ )'
    t.value = str(t.value)
    return t

def t_TS(t):  #\t \n ou espaço
    r'ts'
    t.value = str(t.value)
    return t

def t_CHAV_A(t):  #\t \n ou espaço
    r'{'
    t.value = str(t.value)
    return t

def t_CHAV_F(t):  #\t \n ou espaço
    r'}'
    t.value = str(t.value)
    return t

#def t_SIMBOLO(t):
#    r'[+\-*/.:;_,=[]&/()\\{}\\]' 
#    t.value = str(t.value)
#    return t

def t_REGEX(t): #regex para reconhecer uma regex valida
    #r'^((?:(?:[^?+*{}()[\]\\|]+|\\.|\[(?:\^?\\.|\^[^\\]|[^\\^])(?:[^\]\\]+|\\.)*\]|\((?:\?[:=!]|\?<[=!]|\?>)?\(?1\)??\)|\(\?(?:R|[+-]?\d+)\))(?:(?:[?+*]|\{\d*(?:,\d*)?\})[?+]?)?|\|)*)$'
    #r'[?\w+]?\w+'
    r'ç'
    #r'.+'
    t.value = str(t.value)
    return t

def t_RETURN(t):
    r'return'
    t.value = str(t.value)
    return t


def t_ERROR(t): #erro da gramatica
    r'error'
    t.value = str(t.value)
    return t

def t_error(t): #erro do programa
    print('Illegal character: '+t.value[0])
    t.lexer.skip(1)

t_ignore = ' \n\t'

lexer = lex.lex()