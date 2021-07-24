from rply import LexerGenerator

"""
In order to parse text, you first have to turn that text into individual tokens with a lexer. 
Such a lexer can be generated with the rply.LexerGenerator.

Lexers are generated by adding rules to a LexerGenerator instance. 
Such a rule consists of a name, which will be used as the type of the token generated with that rule, 
and a regular expression defining the piece of text to be matched.

https://rply.readthedocs.io/en/latest/users-guide/lexers.html
"""
class Tokenizer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # operaters
        self.lexer.add('PLUS', r'\+')
        self.lexer.add('MINUS', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('MOD', r'\%')

        self.lexer.add('NUMBER', r'\d+')
        # ignore white space
        self.lexer.ignore('\s+')

        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        self.lexer.add('DISPLAY_STMT', r'print')
        self.lexer.add('SEMI_COLON', r'\;')



    def get_lexer(self):
        # define our patterns or rules for our language
        self._add_tokens()
        # using some re check which all patterns are present in our input string
        return self.lexer.build()
