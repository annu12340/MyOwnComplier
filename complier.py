def tokenizer():
    pass

def parser():
    pass

def transformer():
    pass

def codeGenerator():
    pass

def complier(input_expression):
    tokens=tokenizer(input_expression)
    parser_tree = parser(tokens)
    improved_parse_tree = transformer(parser_tree)
    output = codeGenerator(improved_parse_tree)
    return output
