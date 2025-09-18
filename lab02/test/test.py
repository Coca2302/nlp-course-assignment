import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..\lab01\src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..\lab01')))


from lab01.src.preprocessing.simple_tokenizer import SimpleTokenizer
from lab01.src.preprocessing.regex_tokenizer import RegexTokenizer
from lab02.src.representations.count_vectorizer import CountVectorizer
from lab01.src.core.dataset_loaders import DatasetLoaders

def main():
    sample_corpus = [
        "This is a sample document.",
        "This document is another example document.",
        "And this is the third one.",
    ]
    regex_tokenizer = RegexTokenizer()
    count_vectorizer_regex = CountVectorizer(tokenizer=regex_tokenizer)
    vectors_regex = count_vectorizer_regex.fit_transform(sample_corpus)
    
    print("Vocabulary (RegexTokenizer):")
    print(count_vectorizer_regex.vocabulary_)
    print("Vectors (RegexTokenizer):")
    for vector in vectors_regex:
        print(vector)
    
    simple_tokenizer = SimpleTokenizer()
    count_vectorizer_simple = CountVectorizer(tokenizer=simple_tokenizer)
    vectors_simple = count_vectorizer_simple.fit_transform(sample_corpus)
    
    print("\nVocabulary (SimpleTokenizer):")
    print(count_vectorizer_simple.vocabulary_)
    print("Vectors (SimpleTokenizer):")
    for vector in vectors_simple:
        print(vector)


if __name__ == "__main__":
    main()
