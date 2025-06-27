import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_named_entities(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = cleaned_text.encode("ascii", errors="ignore").decode()

    doc = nlp(cleaned_text)
    entities = {}
    for ent in doc.ents:
        entities.setdefault(ent.label_, []).append(ent.text)
    return entities
