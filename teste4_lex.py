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