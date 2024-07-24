''' 
1. Cleaning Text
    make all words in lowercase
    removing punctuation marks
2. Tokenization and Stop words
3. Lemmatization
4. NLP emotion algorithm
'''

import string
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
from emotions import emotions


text = open('read.txt', encoding='utf-8').read().lower()
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

# faster than split method
tokens = word_tokenize(cleaned_text, "english")
final_words = []
for word in tokens:
    if word not in stopwords.words('english'):
        final_words.append(word)

lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)

sentiments = defaultdict(int)
for word in lemma_words:
    if word in emotions:
        feeling = emotions[word]
        sentiments[feeling] += 1

print(sentiments)

# def sentiment_analyse(sentiment_text):
#     score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
#     if score['neg'] > score['pos']:
#         print("Negative Sentiment")
#     elif score['neg'] < score['pos']:
#         print("Positive Sentiment")
#     else:
#         print("Neutral Sentiment")

# sentiment_analyse(cleaned_text)
