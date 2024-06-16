import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

try:
    df = pd.read_csv('C:/Users/kkouache/OneDrive - ETIK ASSURANCE/Documents/data.csv', delimiter=';', encoding='latin1')
except UnicodeDecodeError as e:
    print(f"UnicodeDecodeError: {e}")
except pd.errors.ParserError as e:
    print(f"ParserError: {e}")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

df['cleaned_text'] = df['text'].apply(clean_text)

df['label'] = df['label'].apply(lambda x: 1 if x == 'positif' else 0 if x == 'négatif' else 2)

X_train, X_test, y_train, y_test = train_test_split(df['cleaned_text'], df['label'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
