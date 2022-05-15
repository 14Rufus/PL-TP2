import ply.lex as lex


tokens = ['LEX_T', 
            'YACC_T', 
            'LEFT', 
            'RIGHT', 
            'TS', 
            'CHAVS', 
            'FIM',
            'NEG', 
            'UMINUS', 
            'TVALUE', 
            'QUOTES', 
            'PRINT',
            'TVAR', 
            'TLSKIP', 
            'PERCENTAGEM', 
            'PARRETOA', 
            'PARRETOF', 
            'ASPAS', 
            'PRECEDENCE_T', 
            'PLICA', 
            'LITERALS_T', 
            'IGNORE_T', 
            'TOKENS_T', 
            'GETVAL', 
            'PALMA', 
            'PALMI', 
            'SPECIAL', 
            'REGEX', 
            'RETURN', 
            'ERROR'] 



literals = ['+','-','*','/', '%', '(', ')', ',', '.', '=', ':', '@']

def t_LEX_T(t):
    r'LEX'
    t.value = str(t.value)
    return t

def t_YACC_T(t):
    r'YACC'
    t.value = str(t.value)
    return t

def t_TVALUE(t):
    r',.*?t\.value.*?\)*' 
    t.value = str(t.value)
    return t

def t_CHAVS(t):
    r'\{.*?\}'
    t.value = str(t.value)
    return t

def t_PRECEDENCE_T(t):
    r'precedence\ *'
    t.value = str(t.value)
    return t

def t_QUOTES(t):
    r'"\w.+"'
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

def t_NEG(t): 
    r'neg\ *'
    t.value = str(t.value)
    return t

def t_UMINUS(t):
    r'UMINUS\ *'
    t.value = str(t.value)
    return t


def t_FIM(t):
    r'~~(.| |\n|\t)+?~~'
    t.value = str(t.value)
    return t

def t_PRINT(t):
    r'print'
    t.value = str(t.value)
    return t

def t_GETVAL(t):
    r'getval'
    t.value = str(t.value)
    return t

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

def t_TS(t): 
    r'ts'
    t.value = str(t.value)
    return t 

def t_TVAR(t):  
    r't\[\d\]'
    t.value = str(t.value)
    return t 

def t_TLSKIP(t):
    r't\.lexer\.skip\(1\)'
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

def t_PALMA(t): #PALMA -> palavra maiuscula
    r'[A-Z]+'
    t.value = str(t.value)
    return t

def t_PALMI(t): #PALMI -> palavra minuscula
    r'[a-z]+'
    t.value = str(t.value)
    return t

def t_SPECIAL(t):  #\t \n ou espaço
    r'(\\[tn]|\ )'
    t.value = str(t.value)
    return t

def t_REGEX(t):
    r'@.+@'
    t.value = str(t.value)
    return t


def t_error(t): #erro do programa
    print('Illegal character: '+t.value[0])
    t.lexer.skip(1)

t_ignore = ' \n\t'

lexer = lex.lex()