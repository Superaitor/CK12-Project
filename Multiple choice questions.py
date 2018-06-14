from word_2_vec import main
from nltk.corpus import wordnet as wn
from random import randint
from Most_Similar import main3


def main2():
    x = main()
    i = input("Press 'm' for multiple choice or 'b' for fill in the blank questions")
    if i == "b":
        fill_in_the_blank(x)

    if i == "m":
        multiple_choices(x)


def fill_in_the_blank(x):
    n = 4  # number of questions you want + 1
    words = list()
    while n > 0:
        random = randint(0, 10)
        if x[random] not in words:
            words.append(x[random])
            n -= 1
    for q in words:
        t = False
        y = wn.synsets(q)
        if y:
            sol = y[0].definition()
            while t is False:
                answer = input("Fill in the blank: " + sol + " :")
                if answer == q:
                    print("Correct!")
                    t = True
                else:
                    print("Try again!")


def multiple_choices(x):
    wrong = 0
    incorrect = list()
    n = len(x)  # number of questions you want + 1
    m = 4  # number of multiple choice questions + 1
    tester = m
    words = list()
    end = False

    while n > 0 and end is False:
        random = randint(0, len(x)- 1)
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
        while x < len(answers):
            if x == 0:
                output.append("a) " + answers[x])
                if answers[x] == w:
                    correct_answer = "a"
                x += 1
            if x == 1:
                output.append("\nb) " + answers[x])
                if answers[x] == w:
                    correct_answer = "b"
                x += 1
            if x == 2:
                output.append("\nc) " + answers[x])
                if answers[x] == w:
                    correct_answer = "c"
                x += 1
            if x == 3:
                output.append("\nd) " + answers[x])
                if answers[x] == w:
                    correct_answer = "d"
                x += 1
            if x == 4:
                output.append("\ne) " + answers[x])
                if answers[x] == w:
                    correct_answer = "e"
                x += 1
        t = False
        while t is False:
            controller = 0
            y = wn.synsets(w)
            if y:
                sol = y[0].definition()
                ans = input("Enter the correct letter answer (or 's' to stop): " + sol + " : \n" + ''.join(output))
                if ans == correct_answer:
                    print("Nice!")
                    t = True
                if ans == "s":
                    end = True
                    break
                else:
                    print("Try again!")
                    wrong += 1
                    if controller is 0:
                        incorrect.append(w)
                        controller += 1
            else:
                break
        if end is True:
            break
    print("Good Job, you finished this automated test. You incorrectly answered questions " + str(wrong) + " times.")
    print("Given your performance in this test, you should practice learning more about:")
    for words in incorrect:
        print("- " + words)
