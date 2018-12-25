import nltk
import collections
import numpy as np
import matplotlib.pyplot as plt
import sys

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


Obama_Text = open(sys.argv[1], "r")
Trump_Text = open(sys.argv[2], "r")

Obama_r = Obama_Text.read()
Trump_r = Trump_Text.read()

stop_words = set(stopwords.words('english'))

#Remove punctuation

tokenizer = RegexpTokenizer(r'\w+')
Obama_tokens = tokenizer.tokenize(Obama_r)
Trump_tokens = tokenizer.tokenize(Trump_r)

# Get clean tokens
Obama_tokens = [t for t in Obama_tokens if not t in stop_words]
Trump_tokens = [t for t in Trump_tokens if not t in stop_words]

# Processing Lexical Diversity

#Obama
st = len(set(Obama_tokens))
lt = len(Obama_tokens)
y = [st*100/lt]
print("Obama Lexical Diversity score", y ,"\n")
fig = plt.figure()
ax = fig.add_subplot(111)
N = 1

# necessary variables
ind = np.arange(N)
width = 0.7
rect = ax.bar(ind, y, width, color='Grey')
# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,100)
ax.set_ylabel('Score')
ax.set_title('Lexical Diversity')
xTickMarks = ['Lexical Diversity Meter - Obama']
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0, fontsize=10)
## add a legend
ax.legend( (rect[0], ('') ))
plt.show()

#Trump
st = len(set(Trump_tokens))
lt = len(Trump_tokens)
y = [st*100/lt]
print("Trump Lexical Diversity score", y,"\n")
fig = plt.figure()
ax = fig.add_subplot(111)
N = 1

# necessary variables
ind = np.arange(N)
width = 0.7
rect = ax.bar(ind, y, width, color='Grey')
# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,100)
ax.set_ylabel('Score')
ax.set_title('Lexical Diversity')
xTickMarks = ['Lexical Diversity Meter - Trump']
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0, fontsize=10)
## add a legend
ax.legend( (rect[0], ('') ))
plt.show()


# get tagged tokens - Obama

tagged = nltk.pos_tag(Obama_tokens)
counts = collections.Counter(tag for word,tag in tagged)
counts = dict(counts)
keys = counts.keys()
y_pos = np.arange(len(keys))

plt.bar(list(counts.keys()), counts.values(), color='g')
plt.title("President Obama")
plt.show()


# get tagged tokens - Trump
tagged = nltk.pos_tag(Trump_tokens)
counts = collections.Counter(tag for word,tag in tagged)
counts = dict(counts)
keys = counts.keys()
y_pos = np.arange(len(keys))

plt.bar(list(counts.keys()), counts.values(), color='g')
plt.title("President Trump")
plt.show()

# Top 50 words - Obama
dist = nltk.FreqDist(Obama_tokens)
dist.plot(50, cumulative=False, title="President Obama")

# Top 50 words - Trump
dist = nltk.FreqDist(Trump_tokens)
dist.plot(50, cumulative=False, title="President Trump")


# predict new sentences - Obama

corpus = Obama_r.split()

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])


pairs = make_pairs(corpus)
word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = np.random.choice(corpus)
chain = [first_word]
n_words = 200

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))
print(' '.join(chain))
print("\n")

# predict new sentences - Trump

corpus = Trump_r.split()

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])


pairs = make_pairs(corpus)
word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = np.random.choice(corpus)
chain = [first_word]
n_words = 200

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))
print(' '.join(chain))