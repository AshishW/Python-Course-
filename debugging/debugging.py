# debugging

# linting 
# linting allows us to detects issues in our code

# using IDE/editor
# read errors


#  pdb: python debugger
import pdb

def tp(n1, n2):
    pdb.set_trace() # we can debug in the terminal. Run 'help' to see commands available 
    return n1 + n2

tp(1,'hi')