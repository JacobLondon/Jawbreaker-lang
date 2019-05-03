import re

from token import *
from expression import *

class Lexer:

    def __init__(self, filename=None):
        if filename is not None:
            self.text = open(filename, 'r').readlines()
        else:
            raise Exception('Invalid file name')
        
        self.line = 0
        self.current = self.text[self.line]

    def advance(self):
        self.line += 1
        if self.line >= len(self.text):
            self.current = None
        else:
            self.current = self.text[self.line]

class Parser:

    def __init__(self, lexer):

        self.lexer = lexer

        self.py_program = ''
        self.indentation = 0

    def bw_parens(self):
        start = self.lexer.current.find(tok.LPAREN) + 1
        end = self.lexer.current.rfind(tok.RPAREN)
        statement = self.lexer.current[start:end]
        return statement

    # indent if a begin statement
    def chk_begin(self):
        if tok.BEGIN in self.lexer.current:
            self.indentation += 1

    def parse(self):
        while self.lexer.current is not None:

            self.py_program += TAB * self.indentation

            if FNDEF_RE.match(self.lexer.current):
                self.convert_function_definition()

            elif FNCALL_RE.match(self.lexer.current):
                self.convert_function_call()
            
            elif IF_RE.match(self.lexer.current):
                self.convert_if()

            elif ELSE_RE.match(self.lexer.current):
                self.convert_else()

            elif ASSIGN_RE.match(self.lexer.current):
                self.convert_assignment()

            elif RETURN_RE.match(self.lexer.current):
                self.convert_return()

            elif BEGIN_RE.match(self.lexer.current):
                self.convert_begin()

            elif END_RE.match(self.lexer.current):
                self.convert_end()

            elif PYCALL_RE.match(self.lexer.current):
                self.convert_pycall()

            elif COMMENT_RE.match(self.lexer.current):
                self.convert_comment()

            self.py_program += '\n'
            self.lexer.advance()

        self.py_program += '\n'
        self.py_program += 'main()'
        print(self.py_program)
        return self.py_program

    # function definition
    def convert_function_definition(self):

        line = ''
        # fn definition
        line += pytok.DEF
        line += SPACE

        # function name
        fname_start = self.lexer.current.find(tok.FN) + len(tok.FN)
        fname_end = self.lexer.current.find(tok.LPAREN)
        fname = self.lexer.current[fname_start:fname_end].lstrip()
        line += fname

        # function args
        line += pytok.LPAREN
        line += self.bw_parens()
        line += pytok.RPAREN
        line += pytok.COLON

        self.py_program += line

        # look for begin
        self.chk_begin()

    # call to a function
    def convert_function_call(self):

        line = ''

        # get function name
        fname_end = self.lexer.current.find(tok.LPAREN)
        fname = self.lexer.current[:fname_end].lstrip()
        line += fname

        # args between parentheses
        line += pytok.LPAREN
        line += self.bw_parens()
        line += pytok.RPAREN

        self.py_program += line

    def convert_if(self):

        line = ''

        # the word 'if'
        if_start = self.lexer.current.find(tok.IF)
        if_end = self.lexer.current.find(tok.LPAREN)
        if_ = self.lexer.current[if_start:if_end]
        self.py_program += if_
        self.py_program += SPACE

        # conditional statement in parentheses
        conditions = self.bw_parens()
        self.py_program += conditions

        self.py_program += pytok.COLON

        # look for begin
        self.chk_begin()

    def convert_else(self):

        # the word 'else'
        line = ''
        line += pytok.ELSE
        line += pytok.COLON

        self.py_program += line
        
        self.chk_begin()

    # an assignment statement
    def convert_assignment(self):

        # variable name
        line = ''
        var_name_end = self.lexer.current.find(tok.EQUAL)
        var_name = self.lexer.current[:var_name_end].lstrip()
        line += var_name

        # apply assignment operator
        line += pytok.EQUAL

        # statement between = and
        statement_start = self.lexer.current.find(tok.EQUAL) + 1
        statement = self.lexer.current[statement_start:].replace('\n', '')
        line += statement

        self.py_program += line

    # a return statement
    def convert_return(self):

        # return word
        line = ''
        line += pytok.RETURN

        # return statement
        state_start = self.lexer.current.find(tok.RETURN) + len(tok.RETURN)
        state = self.lexer.current[state_start:]
        line += state

        self.py_program += line

    # begin by itself
    def convert_begin(self):
        self.indentation += 1

    # end by itself
    def convert_end(self):
        if self.indentation > 0:
            self.indentation -= 1

    # put the python into the code
    def convert_pycall(self):

        line = ''
        py_start = self.lexer.current.find(tok.PYCALL) + 1
        py = self.lexer.current[py_start:]
        line += py
        
        self.py_program += line

    def convert_comment(self):

        # convert comment
        line = ''
        line += pytok.COMMENT

        comment_start = self.lexer.current.find(tok.COMMENT) + len(tok.COMMENT)
        comment = self.lexer.current[comment_start:-1]
        comment.replace('\n', EMPTY)

        line += comment
        self.py_program += line
