from tokenize import TokenInfo
import _tokenize as __tokenize
def _tokenize(readline, encoding):
    tok = __tokenize.TokenizerIter(readline, "utf-8")
    for t in tok:
        str, type,  lineno, end_lineno, col_offset, end_col_offset, line = t
        yield TokenInfo(type, str, (lineno, col_offset), (end_lineno, end_col_offset), line)

def generate_tokens(readline):
    """Tokenize a source reading Python code as unicode strings.
    This has the same API as tokenize(), except that it expects the *readline*
    callable to return str objects instead of bytes.
    """
    return _tokenize(readline, None)


string = 'rf"\\N{bullet}"'

import io
f = io.StringIO(string)
tokens = generate_tokens(f.readline)
for token in tokens:
    print(token)
