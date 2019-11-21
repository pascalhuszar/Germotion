import string
import sys
from nltk.data import load
from nltk.tokenize.treebank import TreebankWordTokenizer
from pathlib import Path

# Sentiment analysis script for german language. This script works with a rule-based approach, using a dictionary.
# Negation handling, like: "Ich mag dich nicht" will be detected.
# It still need further improvments. It's a rudimentary approach.
# created by phuszár

# Variables
datafolder = Path("data/")


def positive_sentiment(query):
    return (analyze(query, 'SentiWS_v2.0_Positive.txt'))


def negative_sentiment(query):
    return analyze(query, 'SentiWS_v2.0_Negative.txt')

# tokenizer
def treebank_tokenizer(sentence):
    tokenizer = load('data/german.pickle')
    treebank_word_tokenize = TreebankWordTokenizer().tokenize
    tokens = []
    for s in tokenizer.tokenize(sentence):
        tokens.extend([token for token in treebank_word_tokenize(s)])
    tokens = [''.join(i for i in s if i not in string.punctuation)
              for s in tokens]
    tokens = list(filter(None, tokens))
    return tokens


# Check for matches in Dictionaries
def analyze(query, dict):
    tokens = treebank_tokenizer(query)
    tokens = stopword_filter(tokens)
    dict = datafolder / dict
    sentiment_value = 0.0
    negative = negation_words()
    with open(dict, 'r', encoding='utf-8') as sentis:
        for s in sentis:
            cells = s.split('\t')
            lemma = cells[0].split('|')
            value = float(cells[1].strip())
            try:
                infl = cells[2].split(',')
                # delete the \n in the last word
                infl[len(infl) - 1] = infl[len(infl) - 1].strip()
            except IndexError:
                infl = []
            for j in tokens:
                if j in infl or j in lemma:
                    try:
                        if tokens[tokens.index(j) - 1] in negative:
                            sentiment_value += value * -0.5
                        elif tokens[tokens.index(j) + 1] in negative:
                            sentiment_value += value * -0.5
                        else:
                            sentiment_value += value
                    except IndexError:
                        sentiment_value += value
    return sentiment_value


# return a list without needless stopwords, like articles, names, pronouns etc.
def stopword_filter(query):
    file_to_open = datafolder / 'stopWords.txt'
    with open(file_to_open, 'r', encoding='utf-8') as f:
        stopWords = [''.join(t)
                     for t in f]
        for i, s in enumerate(stopWords):
            stopWords[i] = s.strip()
    return list(filter(None, [''.join(q for q in t if t not in stopWords)
                              for t in query]))


# return negation words, like: "nie", "nicht", "nein". Needed for negation handling
def negation_words():
    negdict = datafolder / 'negationswoerter.txt'
    with open(negdict, 'r', encoding='utf-8') as negwords:
        negwords = [''.join(n)
                    for n in negwords]
        for i, s in enumerate(negwords):
            negwords[i] = s.strip()
    return negwords


# for flask
def main(query):
    value = round(positive_sentiment(query) + negative_sentiment(query), 2)
    # lambda function for set the value in interval of [-1 to 1]
    value = (lambda x: x if -1.0 < x < 1.0 else (1.0 if x > 1.0 else -1.0))(value)
    return {'sentiment': value}


if __name__ == '__main__':
    print('Use test in comments in code')
    testQuery = "Jede gute Sache im Leben, jeder Sieg der Liebe über den Hass, der Gerechtigkeit über die Ungerechtigkeit, der Gleichheit und Brüderlichkeit über die Ausbeutung, der Eintracht über die Zwietracht, gibt Zeugnis für die Auferstehung in unserem Leben."
    print(main(testQuery))
