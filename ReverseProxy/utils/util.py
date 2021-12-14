# for processing User agent in ml model
import string
ua_punctuation = string.punctuation.replace(".","")

def process_ua(ua : str):
    temp = [c for c in ua if c not in ua_punctuation ]
    punc_removed_ua = "".join(temp).lower()
    punc_removed_ua.split()

    #removing stop words
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer

    pt = PorterStemmer()
    stopwords_removed_ua = [word for word in punc_removed_ua.split() if word not in stopwords.words('english')]  
    stemmed_ua = [pt.stem(word) for word in stopwords_removed_ua]
    return stemmed_ua