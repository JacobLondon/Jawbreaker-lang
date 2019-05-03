import re

from token import *

# keywords
BEGIN = f'({tok.BEGIN})'
END = f'({tok.END})'

TRUE = f'\b({tok.TRUE})\b'
FALSE = f'\b({tok.FALSE})\b'
NIL = f'\b({tok.NIL})\b'

# general
ALPHA = '[a-zA-Z_]'
ALNUM = '[a-zA-Z_\d]'
FN_NAME = f'{ALPHA}{ALNUM}*'
VAR_NAME = f'{ALPHA}{ALNUM}*(\.{ALNUM})*'

PARENS = f'\{tok.LPAREN}(.*)\{tok.RPAREN}'
