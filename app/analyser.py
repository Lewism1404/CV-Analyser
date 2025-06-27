import spacy
from collections import defaultdict

nlp = spacy.load("en_core_web_sm")
def extract_named_entities(text: str):
    doc = nlp(text)
    labels_to_extract = {"PERSON", "ORG", "GPE", "DATE"}
    entities = defaultdict(list)

    for ent in doc.ents:
        if ent.label in labels_to_extract:
            entities[ent.label].append(ent.text)

    return dict(entities)
