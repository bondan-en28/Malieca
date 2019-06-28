#import another class
from lexer import Lexer
from parse import Parser
from codegen import CodeGen

#Deklarasi variabel fname = "nama file"
fname = "input.lieca"
with open(fname) as f:
    text_input = f.read()  #baca input.lieca sebagai text

#inisiasi lexer, codegenerator, dll
lexer = Lexer().get_lexer()
codegen = CodeGen()
module = codegen.module
builder = codegen.builder
printf = codegen.printf
pg = Parser(module, builder, printf)

#Mengambil token dari lexer
tokens = lexer.lex(text_input)

print (tokens)

#Parsing
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

print (parser)

#Code Generate
codegen.create_ir()
codegen.save_ir("hasil.ll") #output
