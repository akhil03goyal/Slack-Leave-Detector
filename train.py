import spacy
import json
from spacy.training.example import Example
from spacy.util import minibatch

# Load blank spaCy model
nlp = spacy.blank("en")

# Add NER component
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

# Define entity labels
LABELS = ["LEAVE_TYPE", "DATE"]
for label in LABELS:
    ner.add_label(label)

# Load training data
with open("training_data.json", "r") as f:
    TRAINING_DATA = json.load(f)

# Convert training data into spaCy examples
examples = []
for text, annotations in TRAINING_DATA:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    examples.append(example)

# Train the model
optimizer = nlp.begin_training()
for i in range(30):
    losses = {}
    batches = minibatch(examples, size=2)
    for batch in batches:
        nlp.update(batch, drop=0.5, losses=losses)
    print(f"Epoch {i}, Loss: {losses}")

# Save model
nlp.to_disk("output_model")
print("✅ Training complete. Model saved in 'output_model'.")
