import re

CPF_PATTERN = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'
EMAIL_PATTERN = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
PHONE_PATTERN = r'\b\d{2}\s?\d{4,5}-?\d{4}\b'

def extract_regex_features(text):
    return {
        "has_cpf": int(bool(re.search(CPF_PATTERN, text))),
        "has_email": int(bool(re.search(EMAIL_PATTERN, text))),
        "has_phone": int(bool(re.search(PHONE_PATTERN, text)))
    }
