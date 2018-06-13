import csv
import nltk
import codecs
import glob
import pickle
import re
import pprint
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
import gensim, logging
from scipy.spatial.distance import cosine
from gensim import corpora, models
from gensim.models import Word2Vec
from gensim.corpora import Dictionary

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def main():
    s = input("enter link of text you want to find key words of: ")
    f = open(s, "r")
    text = word_tokenize(f.read())
    d = keywords(s)
    k = nltk.pos_tag(text)
    x = cleanup(k)
    y = noun_finder(x)
    z = array_splitter(y)
    m = lda(z)
    t = topic_sorter(m)
    # u = tester()
    u = word2vec(y, t, d)
    #printer(u)
    return u



def cleanup(file):
    x = list()
    y = list()
    stop_words = set(stopwords.words('ck12stopwords'))
    for words in file:
        if (not len(words[0]) < 3 and '-' not in words[0] and '=' not in words[0]
                and '/' not in words[0] and '.' not in words[0] and '%' not in words[0]
                and words[0] not in stop_words):
            x.append(words[0])
            y.append(words[1])
    z = list(zip(x, y))
    return z


def noun_finder(file):
    x = list()
    for words in file:
        if words[1] == "NN":
            x.append(words[0])
    return x


def word2vec(file, topic, key):
    x = list()
    repeats = list()
    n = 0
    total_similarities = list()

    for w in key:
        topic.append(w)
        print(w)

    fd = open('word_vectors.pkl', 'rb')
    word_vectors = pickle.load(fd)

    while n < len(topic):
        i = 0
        for words in file:
            if words not in repeats:
                repeats.append(words)
                if n == 0:
                    total_similarities.append(1 - cosine(word_vectors[words], word_vectors[topic[n]]))
                    # total_similarities.append(model.similarity(words, topic[n]))
                else:
                    total_similarities[i] += cosine(1 - word_vectors[words], word_vectors[topic[n]])
                    # total_similarities[i] += model.similarity(words, topic[n])
                i += 1
        n += 1
    for s in total_similarities:
        s /= len(topic)
    #print(total_similarities)


    repeats = list()
    i = 0
    for words in file:
        if words not in repeats:
            repeats.append(words)
            if total_similarities[i] > 0.3 or words in key:
                x.append(words)
            i += 1
    return x


def tester():
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
    x = model.similarity('Pharmacogenomics', 'polymerase')
    print(x)


def lda(file):
    dictionary = corpora.Dictionary(file)
    corpus = [dictionary.doc2bow(text) for text in file]
    l_d_a = gensim.models.ldamodel.LdaModel
    ldamodel = l_d_a(corpus, num_topics=1, id2word=dictionary, passes=50)
    topics = ldamodel.print_topics(num_topics=3, num_words=3)
    return topics


def array_splitter(file):
    size = len(file)
    dubs = []
    adder = []
    i, m, n = 0, 0, 0
    while size > m:

        while i + 5 > m:
            if size > m:
                f = file[m]
                adder.append(f)
                m += 1
            else:
                break
        i = m
        n += 1
        dubs.append(adder)
        adder = []
    return dubs


def topic_sorter(topics):
    splitter = ""
    ind = 0
    tops = []
    separate_words = ""
    odds = 0
    indexes = []
    x = 0
    i = 0
    for word in topics:
        splitter = str(word[1])
    while x < 3:
        if splitter[ind] is '"':
            odds += 1
            if odds % 2 == 1:
                indexes.append(ind)
                x += 1
        ind += 1
    while i < 3:
        for let in splitter[indexes[i] + 1:]:
            if let != '"':
                separate_words += let
            else:
                break
        tops.append(separate_words)
        i += 1
        separate_words = ""
    return tops


def keywords(file_name):
    array = list()
    multiplier = 1
    name = str(file_name)
    lgth = len(name)
    number = 0
    x = lgth - 5
    keys = list()
    while str(9) >= name[x] >= str(0):
        number += (int(name[x]) * multiplier)
        x -= 1
        multiplier *= 10
    with open('artifact_vocabularies.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            array.append(row)
    for key in array:
        if key[0] == str(number) and " " not in key[1]:
            keys.append(key[1])
    return keys


def printer(file):
    for words in file:
        print(words)


#main()
