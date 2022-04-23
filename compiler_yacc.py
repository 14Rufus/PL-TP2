import ply.yacc as yacc
import sys
from compiler_lex import tokens
from compiler_lex import literals

def p_body(p):
    "body : lex"
    
def p_lex(p):
    "lex : PERCENTAGEM PERCENTAGEM LEX_T literals ignore tokens regras "

def p_literals(p):
    "literals : PERCENTAGEM LITERALS_T '=' ASPAS simbolos ASPAS"

def p_simbolos(p):
    "simbolos : simbolos simbolo"

def p_simbolo(p):
    """simbolo : '+'
               | '-'
               | '*'
               | '/'
               | '='
               | '('
               | ')'
               |
    """


def p_simbolos_vazio(p):
    "simbolos : "

def p_ignore(p):
    "ignore : PERCENTAGEM IGNORE_T '=' ASPAS especiais ASPAS"

def p_especiais(p):
    "especiais : especiais SPECIAL"

def p_especiais_vazio(p):
    "especiais : "

def p_tokens(p):
    "tokens : PERCENTAGEM TOKENS_T '=' PARRETOA listatokens PARRETOF"

def p_tokens_vazio(p):
    "tokens : "

def p_listatokens_simples(p):
    "listatokens : PLICA PALM PLICA "

def p_listatokens_recursivo(p):
    "listatokens : listatokens ',' PLICA PALM PLICA  "

def p_regra_return(p):
    "regra : REGEX RETURN '(' ')'"

def p_regra_error(p):
    "regra : REGEX ERROR '(' ')'"

def p_regras(p):
    "regras : regras regra"

def p_regras_vazio(p):
    "regras : "

def p_error(p):
    print("Syntax error! ",p)
    parser.success = False

parser = yacc.yacc()

with open('teste.txt',"r") as f:
    parser.success = True
    data = f.read()
    #print(data)
    result = parser.parse(data)