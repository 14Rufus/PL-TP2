import ply.yacc as yacc

ts={}


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
    if n not in ts:
        print(f"Undefined name '{n}'")
    return ts.get(n,0)
y=yacc()
y.parse("3+4*7")
