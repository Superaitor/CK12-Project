from word_2_vec import cleanup
import pickle
from scipy.spatial.distance import cosine
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


def main3(word):
    # main()
    k = word
    fd = open('word_similarities.pkl', 'rb')
    things = pickle.load(fd)
    words = cleanup(things)
    neighbors = nearest_neighbors(k, words)
    return neighbors


def cleanup(file):
    x = list()
    stop_words = set(stopwords.words('ck12stopwords'))
    for words in file:
        if (not len(words) < 3 and '-' not in words and '=' not in words
                and '/' not in words and '.' not in words and '%' not in words
                and words not in stop_words):
            x.append(words)
    return x


def noun_finder(file):
    x = list()
    for words in file:
        if words[1] == "NN":
            x.append(words[0])
    return x


def nearest_neighbors(k, files):
    stemmer = SnowballStemmer("english")
    fd = open('word_vectors.pkl', 'rb')
    word_vectors = pickle.load(fd)
    total_similarities = {}
    numbers = []
    neighbors = []
    for words in files:
        if words in word_vectors:
            try:
                total_similarities.update({(1 - cosine(word_vectors[words], word_vectors[k])): words})
                numbers.append(1 - cosine(word_vectors[words], word_vectors[k]))
            except KeyError:
                pass

    numbers.sort(reverse=True)
    n = 0
    while n < 4:
        try:
            if stemmer.stem(total_similarities[numbers[n + 10]]) == stemmer.stem(k):
                neighbors.append(total_similarities[numbers[n + 20]])
                n += 1
            else:
                neighbors.append(total_similarities[numbers[n + 10]])
                n += 1
        except KeyError:
            pass
    return neighbors


