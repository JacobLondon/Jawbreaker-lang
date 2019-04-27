import sys, os

from parse import Lexer, Parser

class Arguments:
    def __init__(self, filename, outname=None, run=None):
        self.filename = filename
        self.outname = outname
        self.run = run

def parse_args():

    args = iter(sys.argv)

    # default arguments
    filename = next(args)
    outname = 'a.py'
    run = False

    # default arguments
    arguments = Arguments(filename=next(args))

    # get all arguments
    try:
        for arg in args:

            if arg == '-o':
                outname = next(args)

            elif arg == '-r':
                run = True
    except:
        print('Failure: invalid argument(s)')
        quit()

    # return filtered arguments
    arguments.outname = outname
    arguments.run = run
    return arguments

def jawbreaker():

    # filter arguments
    arguments = parse_args()
    filename = arguments.filename
    outname = arguments.outname
    run = arguments.run

    # generate the code
    l = Lexer(filename)
    p = Parser(l)
    code = p.parse()
    
    # write to the file
    with open(outname, 'w') as out:
        out.write(code)

    # run if specified
    if run:
        os.system('python ' + outname)

if __name__ == '__main__':
    jawbreaker()