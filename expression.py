import re

from token import *

# starting compound expressions
BEGIN_RE = re.compile(f'^\s*({tok.BEGIN})\s*$')

# ending compound expressions
END_RE = re.compile(f'^\s*({tok.END})\s*$')

# function definition
# 'fn e1(anything) begin|newline'
fn_name = '[a-zA-Z][a-zA-Z\d]*?'
FNDEF_RE = re.compile(f'^\s*({tok.FN})\s+{fn_name}\{tok.LPAREN}((.|\n)*)\{tok.RPAREN}(\n|\s*({tok.BEGIN}))\s*$')

# function call
# 'func_name(args)'
FNCALL_RE = re.compile(f'^\s*({fn_name})\s*\{tok.LPAREN}(.*)\{tok.RPAREN}\s*{tok.SEMICOLON}\s*$')

# assignment definition
# 'self.a.b = statement;'
# 'a = statement;'
ASSIGN_RE = re.compile(f'^\s*[a-zA-Z][a-zA-Z\d]*(\.[a-zA-Z\d])*\s*{tok.EQUAL}(.*)\s*{tok.SEMICOLON}\s*$')

# if statement
# if(statement) begin?
IF_RE = re.compile(f'^\s*({tok.IF})\s*\{tok.LPAREN}(.*)\{tok.RPAREN}\s*({tok.BEGIN})?\s*$')

# else statement
# 'else begin' or 'else'
ELSE_RE = re.compile(f'^\s*({tok.ELSE})\s*({tok.BEGIN})?\s*$')

# return statement
# 'return statement';
RETURN_RE = re.compile(f'^\s*({tok.RETURN})\s*(.*)\s*{tok.SEMICOLON}\s*$')

# match a character to keep the line in pure python
PYCALL_RE = re.compile(f'^\s*({tok.PYCALL})\s*(.*)\s*{tok.SEMICOLON}\s*$')
