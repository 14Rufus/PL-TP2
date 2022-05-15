import ply.yacc as yacc
import sys
from compiler_lex import tokens
from compiler_lex import literals

def p_body(p):
    "body : lex yacc funcoes"
    p[0] = p[1] + "\n" + p[2] +"\n" + p[3]



############################### LEX ####################################################
def p_lex(p):
    "lex : PERCENTAGEM PERCENTAGEM LEX_T literals ignore tokens regras_l "
    p[0] = "import ply.lex as lex\n\n" +  p[6] + p[4] + p[5] + p[7] + "\nlexer = lex.lex()"

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
    """
    p[0] = p[1]

def p_simbolos_vazio(p):
    "simbolos : "
    p[0] = ""

def p_ignore(p):
    "ignore : PERCENTAGEM IGNORE_T '=' ASPAS especiais ASPAS"
    p[0] = "\nt_ignore = " + p[4] + " " + p[5] + p[6] + "\n"  

def p_especiais(p):
    "especiais : especiais SPECIAL"
    p[0] = p[1] + p[2]

def p_especiais_vazio(p):
    "especiais : "
    p[0] = ""

def p_tokens(p):
    "tokens : PERCENTAGEM TOKENS_T '=' PARRETOA listatokens PARRETOF"
    p[0] = f"tokens = {p.parser.tokens}\n"

def p_tokens_vazio(p):
    "tokens : "

def p_listatokens_simples(p):
    "listatokens : PLICA PALMA PLICA "
    p.parser.tokens.append(p[2])

def p_listatokens_recursivo(p):
    "listatokens : listatokens ',' PLICA PALMA PLICA"
    p.parser.tokens.append(p[4])


def p_regras_l(p):
    "regras_l : regras_l regra_l"
    p[0] = p[1] + "\n" + p[2]

def p_regras_l_vazio(p):
    "regras_l : "
    p[0] = ""

def p_regra_l_return(p):
    "regra_l : REGEX RETURN '(' PLICA PALMA PLICA TVALUE  "
    aux = "def t_"+p[5]+"(t):\n"
    aux += "\tr'"+p[1][1:len(p[1])-1]+"'\n"
    aux += "\treturn "+p[7][1:len(p[7])-1]+"\n\n"
    p[0] = aux

def p_regra_error(p):
    "regra_l : REGEX ERROR '(' PALMI QUOTES ',' TLSKIP ')'"
    aux = "def t_error(t):\n"
    aux += "\tprint("+p[4] + p[5]+")\n"
    aux += f"\t{p[7]}\n\n"
    p[0] = aux


######################### YACC ############################################


def p_yacc(p):
    "yacc : PERCENTAGEM PERCENTAGEM YACC_T precedence symboltable regras_y"
    p[0] = p[6]

def p_palavra(p):
    """palavra : PALMI
               | PALMA   
    """
    p[0] = p[1]

def p_regras_y(p):
    "regras_y : regras_y regra_y"
    p[0] = p[1] + "\n" +p[2]

def p_regras_y_vazio(p):
    "regras_y : "
    p[0] = ""


def p_precedence(p):
    "precedence : PERCENTAGEM PRECEDENCE_T '=' PARRETOA conteudo_prec PARRETOF"

def p_conteudo_prec(p):
    "conteudo_prec : conteudo_prec tuplo"

def p_conteudo_prec_vazio(p):
    "conteudo_prec : "

def p_tuplo(p):
    "tuplo : '(' lado ',' PLICA simbolo PLICA ',' PLICA simbolo PLICA ')'"

def p_tuplo_2(p):
    "tuplo : '(' lado ',' PLICA UMINUS PLICA ')'"

def p_lado_l(p):
    "lado : PLICA LEFT PLICA"

def p_lado_r(p):
    "lado : PLICA RIGHT PLICA"

def p_symboltable(p):
    "symboltable : TS '=' CHAVS"


def p_regra_y(p):
    "regra_y : PALMI ':' termo CHAVS"
    if p[1] not in p.parser.gramaticas:
        p.parser.gramaticas[p[1]]=0
    else:
        p.parser.gramaticas[p[1]]+=1
    i=p.parser.gramaticas[p[1]]
    if i==0:
        p[0] = f"def p_{p[1]}(t): \n"
    else:
        p[0] = f"def p_{p[1]}_{i}(t): \n"

    p[0] += f'\t"{p[1]} : {p[3]}" \n'
    p[0] += f'\t{p[4][1:len(p[4])-1].strip()} \n' 


#def p_regras_exp_uminus(p):
#    "regra_y : PALMI ':' PLICA '-' PLICA PALMI PERCENTAGEM NEG UMINUS CHAV_A TVAR '=' '-' TVAR CHAV_F"
    #p[0] = 

def p_simbolo_operacao(p):
    """simbolo_operacao : '+'
                        | '-'
                        | '*'
                        | '/'
                        | '='
    """
    p[0] = p[1]

def p_termo_fators(p):
    "termo : fator" 
    p[0] = p[1]  

def p_termo(p):
    "termo : termo PLICA simbolo_operacao PLICA fator"
    p[0] = p[1] + " " + "'" + p[3] + "'" + " " + p[5]


def p_fator(p):
    "fator : palavra "
    p[0] = p[1]

def p_fator_termo(p):
    "fator : PLICA '(' PLICA termo PLICA ')' PLICA" 
    p[0] = p[4]


def p_funcoes(p):
    "funcoes : FIM"
    p[0] = p[1][2:len(p[1])-2]

def p_error(p):
    print("Syntax error! ",p)
    parser.success = False

parser = yacc.yacc()
parser.tokens = []
parser.gramaticas = {}


#with open('teste4.txt',"r") as f:
#    parser.success = True
#    data = f.read()
#    result = parser.parse(data)
#    #print(result)


q = 0

while q == 0:
    inputFile = input('File to read >> ')
    try:
        file = open(inputFile, 'r')
        q = 1
    except OSError:
        print('Ficheiro inválido')

fileOutput = input('Output file >> ')
fileOut = open(fileOutput, 'w+')

fileData = file.read()
result = parser.parse(fileData)
fileOut.write(result)

file.close()
fileOut.close()