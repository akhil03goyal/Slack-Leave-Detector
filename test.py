import spacy
import sys

# Load trained model
nlp = spacy.load("output_model")

# Get message from command-line arguments
if len(sys.argv) > 2 and sys.argv[1] == "--message":
    message = sys.argv[2]
else:
    message = "I'll be on leave tomorrow and Friday"

# Process the message using the model
doc = nlp(message)

print("\nEntities detected:")
for token in doc:
    print(f"Token: {token.text}, Entity: {token.ent_type_}")

# Print recognized named entities
print("\nNamed Entities:")
for ent in doc.ents:
    print(f"{ent.label_}: {ent.text}")
