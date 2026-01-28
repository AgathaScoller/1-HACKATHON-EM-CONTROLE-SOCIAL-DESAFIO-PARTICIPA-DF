import pandas as pd
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, f1_score
from preprocessing import clean_text
from regex_features import extract_regex_features

df = pd.read_csv("data/exemplo_dados.csv")

df["texto"] = df["texto"].apply(clean_text)

regex_df = df["texto"].apply(extract_regex_features).apply(pd.Series)

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
X_text = vectorizer.fit_transform(df["texto"])

X = np.hstack([X_text.toarray(), regex_df.values])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print("F1-score:", f1_score(y_test, y_pred))

joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
