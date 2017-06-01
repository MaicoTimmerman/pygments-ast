from pygments.lexer import RegexLexer, words
from pygments.token import (Text, String, Keyword, Literal, Punctuation, Name,
                            Number, Comment)


class ASTLexer(RegexLexer):
    name = 'AST'
    aliases = ['ast']
    filenames = ['*.ast']

    tokens = {
        'root': [
            (words(("phase", "pass", "node", "nodeset", "traversal",
                    "attributes", "children", "construct", "cycle", "enum",
                    "mandatory", "nodes", "passes", "phases", "prefix",
                    "subphases", "to", "values", "info", "func", "root",),
                   suffix=r'\s*($|(?=[^\w\-]))'), Keyword),
            (words(("double", "float", "int", "uint", "int8", "int16",
                    "int32", "int64", "uint8", "uint16", "uint32", "uint64",
                    "string", "bool")), Keyword.Type),
            (words(("false", "true", "NULL")), Name.Builtin),
            (words(("(", ")", "[", "]", "{", "}", ",", "=", ";", "!")),
             Punctuation),
            (r'[A-Za-z][A-Za-z0-9_]*', Name),
            (r'-?[0-9]+\.[0-9]+', Number.Float),
            (r'[-][0-9]+', Number.Integer),
            (r'\"(\\.|[^\\"])*\"', String),
            (r'/\*', Comment.Multiline, 'comment'),
            (r'//.*?$', Comment.Singleline),
            (r'.', Text)
        ],
        'comment': [
            (r'[^*/]', Comment.Multiline),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline)
        ]
    }
