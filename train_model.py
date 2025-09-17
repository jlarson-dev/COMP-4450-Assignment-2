import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('IMDB Dataset.csv')

x = df['review']
y = df['sentiment']

# Transformer Pipeline
sentiment_classifier = Pipeline([
    ('tfidv', TfidfVectorizer()),
    ('multinb', MultinomialNB())
])

sentiment_classifier.fit(x, y)

# Save model
joblib.dump(sentiment_classifier, 'sentiment_model.pkl')
