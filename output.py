import ply.lex as lex

tokens = ['VAR', 'NUMBER']
literals = ['+','-','/','*','=','(',')']
t_ignore = " \t\n"

def t_VAR(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	return  t.value


def t_NUMBER(t):
	r'\d+(\.\d+)?'
	return  float(t.value)


def t_error(t):
	print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
	t.lexer.skip(1)


lexer = lex.lex()

def p_stat(t): 
	"stat : VAR '=' exp" 
	ts[t[1]] = t[3] 

def p_stat_1(t): 
	"stat : exp" 
	print(t[1]) 

def p_exp(t): 
	"exp : exp '+' exp" 
	t[0] = t[1] + t[3] 

def p_exp_1(t): 
	"exp : exp '-' exp" 
	t[0] = t[1] - t[3] 

def p_exp_2(t): 
	"exp : exp '*' exp" 
	t[0] = t[1] * t[3] 

def p_exp_3(t): 
	"exp : exp '/' exp" 
	t[0] = t[1] / t[3] 

def p_exp_4(t): 
	"exp : exp" 
	t[0] = t[2] 

def p_exp_5(t): 
	"exp : NUMBER" 
	t[0] = t[1] 

def p_exp_6(t): 
	"exp : VAR" 
	t[0] = getval(t[1]) 


def p_error(t):
    print(f"Syntax error at '{t.value}', [{t.lexer.lineno}]")
def getval(n):
    if n not in ts: print(f"Undefined name '{n}'")
    return ts.get(n,0)
y=yacc()
y.parse("3+4*7")