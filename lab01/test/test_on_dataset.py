import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.core.interfaces import Tokenize
from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.preprocessing.simple_tokenizer import SimpleTokenizer
from src.core.dataset_loaders import DatasetLoaders

def main():
    dataset_path = 'dataset\\UD_English-EWT\\en_ewt-ud-train.txt'
    data_loader = DatasetLoaders(dataset_path)
    raw_text = data_loader.load_raw_text_data()
    test_length = 100
    
    if raw_text is None:
        return
    
    print("Raw Text:")
    print(raw_text[:test_length])
    
    regex_tokenizer = RegexTokenizer()
    regex_tokens = regex_tokenizer.tokenize(raw_text[:test_length])
    print("\nTokens using RegexTokenizer:")
    print(regex_tokens)
    
    simple_tokenizer = SimpleTokenizer()
    simple_tokens = simple_tokenizer.tokenize(raw_text[:test_length])
    print("\nTokens using SimpleTokenizer:")
    print(simple_tokens)

if __name__ == "__main__":
    main()
