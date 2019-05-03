import re

from token import *
from keyword_format import *

# starting compound expressions
BEGIN_RE = re.compile(f'^\s*{BEGIN}\s*$')

# ending compound expressions
END_RE = re.compile(f'^\s*{END}\s*$')

# function definition
# 'fn e1(anything) begin|newline'
FNDEF_RE = re.compile(f'^\s*({tok.FN})\s+({FN_NAME})\s*({PARENS})(\s*({tok.BEGIN}))?\s*$')

# function call
# 'func_name(args)'
FNCALL_RE = re.compile(f'^\s*({FN_NAME})\s*({PARENS})\s*$')

# assignment definition
# 'self.a.b = statement'
# 'a = statement;'
ASSIGN_RE = re.compile(f'^\s*({VAR_NAME})\s*({tok.EQUAL})(.*)$')

# if statement
# if(statement) begin?
IF_RE = re.compile(f'^\s*({tok.IF})\s*({PARENS})\s*({tok.BEGIN})?\s*$')

# else statement
# 'else begin' or 'else'
ELSE_RE = re.compile(f'^\s*({tok.ELSE})\s*({tok.BEGIN})?\s*$')

# return statement
# 'return statement'
RETURN_RE = re.compile(f'^\s*({tok.RETURN})\s*(.*)\s*$')

# match a character to keep the line in pure python
PYCALL_RE = re.compile(f'^\s*({tok.PYCALL})\s*(.*)\s*$')

# match a comment character
COMMENT_RE = re.compile(f'^\s*({tok.COMMENT})(.*)$')
