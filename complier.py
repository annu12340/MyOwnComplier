import copy
import re

def tokenizer(input_expression):
    token = []
    current_position = 0
    alphabet_pattern = re.compile(r"[a-z]", re.I);
    numbers_pattern = re.compile(r"[0-9]");
    whiteSpace_pattern = re.compile(r"\s");
    
    for char in  input_expression:
        # skip white spaces
        if re.match(whiteSpace_pattern,char):
            continue
        elif char == '(':
            tokens.append({
                'type': 'left_paren',
                'value': '('
            })
        elif char == ')':
            tokens.append({
                'type': 'right_paren',
                'value': ')'
            })
        elif re.match(numbers_pattern, char):
            # it can be 1 digit or more than 1 digit
            full_number = ''
            while re.match(numbers_pattern, char):
                full_number += char
            tokens.append({
                'type': 'number',
                'value': full_number
            })
        
        elif re.match(numbers_pattern, char):
            # it can be 1 letter or more than 1 letter
            full_letter = ''
            while re.match(alphabet_pattern, char):
                full_letter += char
            tokens.append({
                'type': 'number',
                'value': full_letter
            })
    return token
    
def parser():
    pass

def transformer():
    pass

def codeGenerator():
    pass

def complier(input_expression):
    input_expression
    tokens=tokenizer(input_expression)
    print('tokens',tokens)
    parser_tree = parser(tokens)
    improved_parse_tree = transformer(parser_tree)
    output = codeGenerator(improved_parse_tree)
    return output
