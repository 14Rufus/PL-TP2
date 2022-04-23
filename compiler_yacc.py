import ply.yacc as yacc
import sys
from compiler_lex import tokens
from compiler_lex import literals

def p_body(p):
    "body : lex yacc"



############################### LEX ####################################################
def p_lex(p):
    "lex : PERCENTAGEM PERCENTAGEM LEX_T literals ignore tokens regras_l "

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
    "regra_l : REGEX RETURN '(' ')'"

def p_regra_error(p):
    "regra_l : REGEX ERROR '(' ')'"

def p_regras_l(p):
    "regras_l : regras_l regra_l"

def p_regras_vazio(p):
    "regras_l : "

######################### YACC ############################################

def p_yacc(p):
    "yacc : PERCENTAGEM PERCENTAGEM YACC_T precedence symboltable regras_y"

def p_precedence(p):
    "precedence : PERCENTAGEM PRECEDENCE_T '=' PARRETOA conteudo_prec PARRETOF"

def p_conteudo_prec(p):
    "conteudo_prec : tuplo ',' tuplo ',' tuplo_2 ','"

def p_tuplo(p):
    "tuplo : '(' lado ',' PLICA simbolo PLICA ',' PLICA simbolo PLICA ')'"

def p_tuplo_2(p):
    "tuplo_2 : '(' lado ',' PLICA UMINUS PLICA ')'"

def p_lado_l(p):
    "lado : PLICA LEFT PLICA"

def p_lado_r(p):
    "lado : PLICA RIGHT PLICA"

def p_symboltable(p):
    "symboltable : TS '=' CHAV_A CHAV_F"


########### REVER
def p_regras_stat(p):
    "regras_y : STAT ':' PALM PLICA '=' PLICA EXP CHAV_A CHAV_F"  

def p_regras_stat_e(p):
    "regras_y : STAT ':' EXP CHAV_A CHAV_F"


def p_regras_exp_add(p):
    "regras_y : EXP ':' EXP PLICA '+' PLICA EXP CHAV_A CHAV_F"

def p_regras_exp_sub(p):
    "regras_y : EXP ':' EXP PLICA '-' PLICA EXP CHAV_A CHAV_F"

def p_regras_exp_mul(p):
    "regras_y : EXP ':' EXP PLICA '*' PLICA EXP CHAV_A CHAV_F"

def p_regras_exp_div(p):
    "regras_y : EXP ':' EXP PLICA '/' PLICA EXP CHAV_A CHAV_F"

def p_regras_exp_uminus(p):
    "regras_y : EXP ':' PLICA '-' PLICA EXP PERCENTAGEM NEG UMINUS CHAV_A CHAV_F"

def p_regras_exp_par(p):
    "regras_y : EXP ':' PLICA '(' PLICA EXP PLICA ')' PLICA CHAV_A CHAV_F"

def p_regras_exp_num(p):
    "regras_y : EXP ':' PALM CHAV_A CHAV_F"

#igual à de cima
#def p_regras_exp_var(p):
    #"regras_y : EXP ':' PALM CHAV_A CHAV_F"




def p_error(p):
    print("Syntax error! ",p)
    parser.success = False

parser = yacc.yacc()

with open('teste3.txt',"r") as f:
    parser.success = True
    data = f.read()
    #print(data)
    result = parser.parse(data)