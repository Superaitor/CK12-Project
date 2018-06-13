from word_2_vec import main
from nltk.corpus import words as wds
from nltk.corpus import wordnet as wn
from random import randint
from Most_Similar import main3
from gensim.models import word2vec


def main2():
    x = main()
    i = input("Press 'm' for multiple choice or 'b' for fill in the blank questions")
    if i == "b":
        fill_in_the_blank(x)

    if i == "m":
        multiple_choices(x)


def fill_in_the_blank(x):
    correct_answer = " "
    n = 4  # number of questions you want + 1
    m = 4  # number of multiple choice questions + 1
    tester = m
    words = list()
    quests = [None] * n
    answers = [None] * (tester + 1)
    while n > 0:
        random = randint(0, 10)
        if x[random] not in words:
            words.append(x[random])
            n -= 1
    for q in words:
        y = wn.synset(q + '.n.01').definition()
        t = False
        while(t is False):
            answer = input("Fill in the blank: " + y + " :")
            if answer == q:
                print("Correct!")
                t = True
            else:
                print("Try again!")


def multiple_choices(x):
    n = 4  # number of questions you want + 1
    m = 4  # number of multiple choice questions + 1
    tester = m
    words = list()
    quests = [None] * n

    while n > 0:
        random = randint(0, 10)
        if x[random] not in words:
            words.append(x[random])
            n -= 1
    for w in words:
        correct_answer = " "
        answers = [None] * (tester + 1)
        answers[randint(0, 4)] = w
        a = main3(w)
        lgth = 3
        while lgth >= 0:
            r = randint(0, 4)
            if answers[r] is None:
                answers[r] = a[lgth]
                lgth -= 1
        x = 0
        output = list()
        while (x < len(answers)):
            if x == 0:
                output.append("a: " + answers[x])
                if answers[x] == w:
                    correct_answer = "a"
                x += 1
            if x == 1:
                output.append("b: " + answers[x])
                if answers[x] == w:
                    correct_answer = "b"
                x += 1
            if x == 2:
                output.append("c: " + answers[x])
                if answers[x] == w:
                    correct_answer = "c"
                x += 1
            if x == 3:
                output.append("d: " + answers[x])
                if answers[x] == w:
                    correct_answer = "d"
                x += 1
            if x == 4:
                output.append("e: " + answers[x])
                if answers[x] == w:
                    correct_answer = "e"
                x += 1
        t = False
        while t is False:
            y = wn.synset(w + '.n.01').definition()
            print(output)
            ans = input("Enter the correct letter answer: " + y + " : ")
            if ans == correct_answer:
                print("Nice!")
                t = True
            else:
                print("Try again!")


main2()
