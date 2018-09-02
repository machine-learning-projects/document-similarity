# Based on the implementation found at https://stackoverflow.com/a/8897648

from sklearn.feature_extraction.text import TfidfVectorizer

text_files = ['../data/nowIsTheTime.txt', '../data/quickBrownFox.txt']
documents = [open(f, encoding="utf8").read() for f in text_files]
tfidf = TfidfVectorizer().fit_transform(documents)
# no need to normalize, since Vectorizer will return normalized tf-idf
pairwise_similarity = (tfidf * tfidf.T).A

print(pairwise_similarity)
