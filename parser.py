import ply.lex as lex


# Feature description language (FDL) Tokens
tokens = (
    'STRING', 'NUMBER', 'TWO_DOTS', 'COMMA', 'OPEN_PARENTHESES', 'CLOSE_PARENTHESES', 'HYPHEN'
)


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_STRING = r'[a-zA-Z]+'
t_TWO_DOTS = r'\:'
t_COMMA = r'\,'
t_OPEN_PARENTHESES = r'\('
t_CLOSE_PARENTHESES = r'\)' 
t_HYPHEN = r'\-'

# Ignored characters
t_ignore = " \t\n"



def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Testing the tokens

lexer.input("Bicycle : all (Frame, Gear, opt (Accessory)")

while True:
    tok = lexer.token()
    if not tok:
        print("\n")
        break      # No more input
    print(tok)


# Parsing rules
import ply.yacc as yacc

# initialize the diagram
print("digraph {" + "\n"  )


def p_def_def(p):
    'def :  assigns'
    print("}")


def p_def_assigns(p):
    '''assigns : assign
               | assigns assign'''

    

# A complete FDL expression
def p_assign(p):
    '''assign : init_graphviz contraint OPEN_PARENTHESES expr CLOSE_PARENTHESES'''


# FDL Main component (ex: Bicycle :)
def p_init_graphviz(p):
    'init_graphviz : STRING TWO_DOTS'
    global top_object 
    top_object = p[1]
    print(top_object, "[shape = box]" + "\n")



# FDL component relation (ex: all, one-of and more-of)
def p_contraint(p):
    '''contraint : STRING HYPHEN STRING
                 | STRING '''
    global contraint
    contraint = p[1]


def p_def_expr(p):
    'expr : components'


# Components inside expression
def p_components(p):
    '''components : STRING COMMA components
                | NUMBER COMMA components
                | opt_case COMMA components
                | STRING
                | NUMBER
                | opt_case'''
    for i in p:
        if i is not None and i != ",":
         print(i, "[shape = box]" + "\n")
         print(top_object, "->", i, "[arrowhead = dot]" + "\n")


# Optional component
def p_opt_case(p):
    'opt_case : STRING OPEN_PARENTHESES STRING CLOSE_PARENTHESES'
    print(top_object, "->", p[3], "[arrowhead = odot]" + "\n")

   
    
def p_error (t): 
 print("Syntax error at '%s'" % t.value)


# Build the parser
parser = yacc.yacc()

import sys
if len(sys.argv) < 2 :
 sys.exit("Usage: %s <filename>" % sys.argv[0])

fp = open(sys.argv[1])

contents = fp.read()
result = parser.parse(contents)


