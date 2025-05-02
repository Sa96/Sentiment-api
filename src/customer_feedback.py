import requests
import pandas as pd
from datetime import datetime
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

data = {
    	'text': ['I love this product!', 'Worst experience ever.', 'Not bad', 'Absolutely fantastic!', 'Terrible service'],
    	'label': [1, 0, 1, 1, 0]
	}
df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

logistic_regression = LogisticRegression()
logistic_regression.fit(X,y)

joblib.dump(logistic_regression, 'model/model.joblib')
joblib.dump(vectorizer, 'model/vectorizer.joblib')
