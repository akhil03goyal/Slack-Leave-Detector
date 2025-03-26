import spacy
from spacy.tokens import DocBin
import json

nlp = spacy.blank("en")
db = DocBin()

with open("training_data.json", "r") as f:
    TRAINING_DATA = json.load(f)

for text, annotations in TRAINING_DATA:
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annotations["entities"]:
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span:
            ents.append(span)
    doc.ents = ents
    db.add(doc)

db.to_disk("training_data.spacy")
