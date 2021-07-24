from tokenizer import Tokenizer

my_high_level_program = """
print(4 + 4 - 2);
"""

def complier():
    # STEP 1
    tokenization = Tokenizer().get_lexer()
    tokens = tokenization.lex(my_high_level_program)
    for token in tokens:
        print(token)
    print('tokens',tokens)
    # parser_tree = parser(tokens)
    # improved_parse_tree = transformer(parser_tree)
    # output = codeGenerator(improved_parse_tree)
    # return output
complier()
