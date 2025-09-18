from src.core.interfaces import Tokenize

class RegexTokenizer(Tokenize):
    def tokenize(self, text: str):
        import re
        tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
        return tokens
    
