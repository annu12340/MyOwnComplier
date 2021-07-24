from rply import ParserGenerator
from ast import Number, Sum, Sub, Mul, Print

"""
 we will generate a parser for simple mathematical expressions that has only +,* and -
 as defined by the following the grammar:
 <expression> ::= "\d+"
               | <expression> "+" <expression>
               | <expression> "-" <expression>
               | <expression> "*" <expression>
               | "(" <expression> ")"


Here production rules define a sequence of terminals (tokens) and non-terminals using the production() decorator.
"""
class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'PLUS', 'MINUS', 'MUL']
        )

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(p[2])

        @self.pg.production('expression : expression PLUS expression')
        @self.pg.production('expression : expression MINUS expression')
        @self.pg.production('expression : expression MUL expression')
        def expression(p):
            # it is infix notation a + b. So the operands are on the both sides
            left_operand = p[0]
            right_operand = p[2]
            operator = p[1]
            if operator.gettokentype() == 'PLUS':
                return Sum(left_operand, right_operand)
            elif operator.gettokentype() == 'MINUS':
                return Sub(left_operand, right_operand)
            elif operator.gettokentype() == 'MUL':
                return Mul(left_operand, right_operand)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())


    def get_parser(self):
        return self.pg.build()

