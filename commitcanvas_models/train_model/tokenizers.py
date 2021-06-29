import nltk
from nltk.corpus import stopwords

def stem_tokenizer(text):
    '''
    Tokenize the given text, keep alpha tokens, remove stopwords and perform stemming

    input: commit message subject

    output: tokens
    '''
    ps = nltk.PorterStemmer()
    tokens = [word for word in nltk.word_tokenize(text) if (word.isalpha() and word not in stopwords.words('english'))] 
    stems = [ps.stem(item) for item in tokens]
    return stems

def dummy(doc):
    '''Helper method for scikilearn'''
    return doc