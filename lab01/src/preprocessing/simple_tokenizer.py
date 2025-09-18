from src.core.interfaces import Tokenize

class SimpleTokenizer(Tokenize):
    def tokenize(self, text: str):
        for char in text:
            if char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ':
                text = text.replace(char, f' {char} ')
        return text.strip().split()  
    
