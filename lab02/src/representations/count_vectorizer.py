from lab02.src.core.Vectorizer import Vectorizer
from lab01.src.core.interfaces import Tokenize
from lab01.src.preprocessing.simple_tokenizer import SimpleTokenizer
from lab01.src.preprocessing.regex_tokenizer import RegexTokenizer


class CountVectorizer(Vectorizer):
    
    def __init__(self, tokenizer: Tokenize):
        self.tokenizer = tokenizer
        self.vocabulary_ = {}
    
    def fit(self, corpus: list[str]):
        unique_tokens = set()
        for document in corpus:
            tokens = self.tokenizer.tokenize(document)
            unique_tokens.update(tokens)
        self.vocabulary_ = {token: idx for idx, token in enumerate(sorted(unique_tokens))}
    
    def transform(self, documents: list[str]) -> list[list[int]]:
        vectors = []
        for document in documents:
            vector = [0] * len(self.vocabulary_)
            tokens = self.tokenizer.tokenize(document)
            for token in tokens:
                if token in self.vocabulary_:
                    index = self.vocabulary_[token]
                    vector[index] += 1
            vectors.append(vector)
        return vectors
    
    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        self.fit(corpus)
        return self.transform(corpus)

