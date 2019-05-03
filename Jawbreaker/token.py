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

    # constants
    TRUE            = 'true'
    FALSE           = 'false'
    NIL             = 'nil'

    # symbols
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
    COMMENT         = '--'

    # logic symbols
    LOGAND          = 'and'
    BITAND          = '&'
    LOGOR           = 'or'
    BITOR           = '|'
    NOT             = '!'

class pytok():
    DEF             = 'def'
    ELSE            = 'else'
    RETURN          = 'return'

    # constants
    TRUE            = 'True'
    FALSE           = 'False'
    NONE            = 'None'

    # symbols
    COMMENT         = '#'
    COLON           = ':'
    LPAREN          = '('
    RPAREN          = ')'
    EQUAL           = '='

