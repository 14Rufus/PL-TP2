import ply.yacc as yacc
import sys
from compiler_lex import tokens
from compiler_lex import literals

def p_body(p):
    "body : lex yacc"
    p[0] = p[1]



############################### LEX ####################################################
def p_lex(p):
    "lex : PERCENTAGEM PERCENTAGEM LEX_T literals ignore tokens regras_l "
    p[0] = p[4]

def p_literals(p):
    "literals : PERCENTAGEM LITERALS_T '=' ASPAS simbolos ASPAS"
    aux = "literals = ["
    for i in range(0,len(p[5])-1):
        aux += "'" + p[5][i] + "'" +","
    aux += "'" + p[5][len(p[5])-1] + "'" + "]"
    p[0] = aux

def p_simbolos(p):
    "simbolos : simbolos simbolo"
    p[0] = p[1]+p[2]

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
    p[0] = p[1]

def p_simbolos_vazio(p):
    "simbolos : "
    p[0] = ""

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
    "listatokens : PLICA PALMA PLICA "
    p.parser.tokens.append(p[2])

def p_listatokens_recursivo(p):
    "listatokens : listatokens ',' PLICA PALMA PLICA  "
    p.parser.tokens.append(p[4])


def p_regras_l(p):
    "regras_l : regras_l regra_l"

def p_regras_l_vazio(p):
    "regras_l : "

def p_regra_l_return(p):
    "regra_l : REGEX RETURN '(' ')'"
    #aux = "def t_"+p[4]+"(t):"
    #aux += "\tr'"+p[1]+"'"
    #aux += "\treturn "+p[6]+"\n"

def p_regra_error(p):
    "regra_l : REGEX ERROR '(' ')'"


######################### YACC ############################################

def p_regras_y(p):
    "regras_y : regras_y regra_y"

def p_regras_y_vazio(p):
    "regras_y : "

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
    "regra_y : PALMI ':' PALMA PLICA '=' PLICA PALMI CHAV_A CHAV_F"  

def p_regras_stat_e(p):
    "regra_y : PALMI ':' PALMI CHAV_A CHAV_F"

def p_regras_exp_add(p):
    "regra_y : PALMI ':' PALMI PLICA '+' PLICA PALMI CHAV_A CHAV_F"

def p_regras_exp_sub(p):
    "regra_y : PALMI ':' PALMI PLICA '-' PLICA PALMI CHAV_A CHAV_F"

def p_regras_exp_mul(p):
    "regra_y : PALMI ':' PALMI PLICA '*' PLICA PALMI CHAV_A CHAV_F"

def p_regras_exp_div(p):
    "regra_y : PALMI ':' PALMI PLICA '/' PLICA PALMI CHAV_A CHAV_F"

def p_regras_exp_uminus(p):
    "regra_y : PALMI ':' PLICA '-' PLICA PALMI PERCENTAGEM NEG UMINUS CHAV_A CHAV_F"

def p_regras_exp_par(p):
    "regra_y : PALMI ':' PLICA '(' PLICA PALMI PLICA ')' PLICA CHAV_A CHAV_F"

def p_regras_exp_num(p):
    "regra_y : PALMI ':' PALMA CHAV_A CHAV_F"

#igual à de cima
#def p_regras_exp_var(p):
    #"regras_y : EXP ':' PALM CHAV_A CHAV_F"




def p_error(p):
    print("Syntax error! ",p)
    parser.success = False

parser = yacc.yacc()
parser.tokens = []


with open('teste4.txt',"r") as f:
    parser.success = True
    data = f.read()
    #print(data)
    result = parser.parse(data)
    print(parser.tokens)
    print(result)