from enum import Enum

SPACE = ' '
EMPTY = ''
TAB = ' ' * 4

# words
class tok():
    BEGIN           = 'begin'
    END             = 'end'
    FN              = 'fn'
    IF              = 'if'
    ELSE            = 'else'
    FOR             = 'for'
    WHILE           = 'while'
    RETURN          = 'return'
    CONTINUE        = 'continue'
    BREAK           = 'break'

    # 1 char symbol
    SEMICOLON       = ';'
    LPAREN          = '('
    RPAREN          = ')'
    PLUS            = '+'
    MINUS           = '-'
    ASTRISK         = '*'
    FSLASH          = '/'
    MODULUS         = '%'
    EQUAL           = '='
    PYCALL          = '`'

    # multi char symbol
    LOGAND          = 'and'
    BITAND          = '&'
    LOGOR           = 'or'
    BITOR           = '|'
    NOT             = '!'

class pytok():
    DEF             = 'def'
    ELSE            = 'else'
    RETURN          = 'return'

    COLON           = ':'
    LPAREN          = '('
    RPAREN          = ')'

