import spacy
import json
from spacy.training.example import Example
from spacy.util import minibatch

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner", last=True)

LABELS = ["LEAVE_TYPE", "DATE"]

for label in LABELS:
    ner.add_label(label)

nlp.begin_training()
with open("training_data.json", "r") as f:
    TRAINING_DATA = json.load(f)

examples = []
for text, annotations in TRAINING_DATA:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    examples.append(example)

for i in range(30):
    losses = {}
    batches = minibatch(examples, size=2)
    for batch in batches:
        nlp.update(batch, drop=0.5, losses=losses)
    print(f"Epoch {i}, Loss: {losses}")

nlp.to_disk("output_model")
print("Training complete. Model saved in 'output_model'.")
