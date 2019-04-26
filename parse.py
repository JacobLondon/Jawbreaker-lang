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
        #print(self.py_program)
        return self.py_program

    # function definition
    def convert_function_definition(self):

        # function definition
        self.py_program += pytok.DEF

        # function name
        fname_start = self.lexer.current.find(SPACE)
        fname_end = self.lexer.current.find(tok.LPAREN)
        fname = self.lexer.current[fname_start:fname_end]
        self.py_program += fname

        # function args
        self.py_program += pytok.LPAREN
        args = self.bw_parens()
        self.py_program += args
        self.py_program += pytok.RPAREN

        self.py_program += pytok.COLON

        # look for begin
        self.chk_begin()

    # call to a function
    def convert_function_call(self):

        # get function name
        fname_end = self.lexer.current.find(tok.LPAREN)
        fname = self.lexer.current[:fname_end].lstrip()
        self.py_program += fname

        # args between parentheses
        self.py_program += pytok.LPAREN
        args = self.bw_parens()
        self.py_program += args
        self.py_program += pytok.RPAREN

    def convert_if(self):

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
        self.py_program += pytok.ELSE
        self.py_program += pytok.COLON
        
        self.chk_begin()

    # an assignment statement
    def convert_assignment(self):

        # variable name
        var_name_end = self.lexer.current.find(tok.EQUAL)
        var_name = self.lexer.current[:var_name_end].lstrip()
        self.py_program += var_name

        # apply assignment operator
        self.py_program += tok.EQUAL

        # statement between = and ;
        statement_start = self.lexer.current.find(tok.EQUAL) + 1
        statement_end = self.lexer.current.rfind(tok.SEMICOLON)
        statement = self.lexer.current[statement_start:statement_end]
        self.py_program += statement

    # a return statement
    def convert_return(self):

        # return word
        self.py_program += pytok.RETURN
        self.py_program += SPACE

        # return statement
        state_start = self.lexer.current.find(SPACE) + 1
        state_end = self.lexer.current.find(tok.SEMICOLON)
        state = self.lexer.current[state_start:state_end]
        self.py_program += state

    # begin by itself
    def convert_begin(self):
        self.indentation += 1

    # end by itself
    def convert_end(self):
        if self.indentation > 0:
            self.indentation -= 1

    # put the python into the code
    def convert_pycall(self):

        py_start = self.lexer.current.find(tok.PYCALL) + 1
        py_end = self.lexer.current.find(tok.SEMICOLON)
        py = self.lexer.current[py_start:py_end]
        self.py_program += py

    def convert_comment(self):

        self.py_program += pytok.COMMENT

        comment_start = self.lexer.current.find(tok.COMMENT) + len(tok.COMMENT)
        comment = self.lexer.current[comment_start:-2]
        comment.replace('\n', EMPTY)

        self.py_program += comment
