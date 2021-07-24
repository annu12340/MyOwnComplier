from tokenizer import Tokenizer
from parse_tree_generator import Parser
from code_generator import CodeGen


input_program_name = "ente-swanthan-high-level-program.abc"
with open(input_program_name) as f:
    input_program_name = f.read()

# STEP 1 -> Tokenization
lexer = Tokenizer().get_lexer()
tokens = lexer.lex(input_program_name)

# STEP 2 -> Generate parse tree
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

# STEP3 -> Code generation
codegen = CodeGen()
module = codegen.module
builder = codegen.builder
printf = codegen.printf

codegen.create_ir()
# Creates a new file called ente_transformed_low_level_code.xyz with the transformed code
codegen.save_ir("ente_transformed_low_level_code.xyz")
