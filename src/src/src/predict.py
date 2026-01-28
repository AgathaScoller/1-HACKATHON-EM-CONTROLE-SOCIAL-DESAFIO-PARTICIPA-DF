import sys
import joblib
import numpy as np
from preprocessing import clean_text
from regex_features import extract_regex_features

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_text(text):
    text_clean = clean_text(text)
    regex_feats = extract_regex_features(text_clean)
    regex_array = np.array(list(regex_feats.values())).reshape(1, -1)

    text_vec = vectorizer.transform([text_clean]).toarray()
    X = np.hstack([text_vec, regex_array])

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0].max()

    return {
        "classificacao": "dados_pessoais" if pred == 1 else "nao_pessoais",
        "confianca": float(prob),
        "indicios_regex": [k for k, v in regex_feats.items() if v == 1]
    }

if __name__ == "__main__":
    texto_input = " ".join(sys.argv[1:])
    resultado = predict_text(texto_input)
    print(resultado)
