# Reading  the data from input.txt
contents = ""
with open('input.txt', encoding="utf-8") as f:
    for line in f.readlines():
        contents += line
f.close()

# Tokenization
from nltk.tokenize import word_tokenize

tokenized_words = word_tokenize(contents)

# Lemmatization
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
lemmatized_words = [wordnet_lemmatizer.lemmatize(w) for w in tokenized_words]
print("Lemmatized words\n")
print(lemmatized_words)
print("\n")

# Bigrams
from nltk.util import ngrams

bigrams = list(ngrams(tokenized_words, 2))
print("Bigrams\n")
print(bigrams)
print("\n")
# Top 5 Bigrams
import nltk

fdist = nltk.FreqDist(bigrams)
top_5 = fdist.most_common(5)
print("Top 5 bigrams \n ")
print(top_5)
print("\n")

# lines with the top 5 bigrams

summary = ''
for bigram in top_5:
    x = bigram[0][0]
    y = bigram[0][1]
    with open('input.txt', encoding="utf-8") as f:
        for line in f.readlines():
            words = line.strip().split()  # all words on the line
            for word1, word2 in zip(words, words[1:]):  # iterate through pairs
                if word1 == x and word2 == y:
                    summary = summary + line
print("Final only bigrams concatenated summary \n")
print(summary)