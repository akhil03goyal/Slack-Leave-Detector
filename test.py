import spacy
import argparse
from date_preprocessor import resolve_date

# Load trained model
nlp = spacy.load("output_model")

def process_message(message):
    doc = nlp(message)

    # Print token-wise entities
    print("\nEntities detected (Token-wise):")
    for token in doc:
        entity = token.ent_type_ if token.ent_type_ else "None"
        print(f"Token: {token.text}, Entity: {entity}")

    # Extract named entities
    entities = {ent.label_: ent.text for ent in doc.ents}

    print("\nNamed Entities (Span-based):")
    for label, text in entities.items():
        print(f"{label}: {text}")

    # Resolve DATE entity
    if "DATE" in entities:
        resolved_date = resolve_date(entities["DATE"])
        print(f"\nResolved DATE: {resolved_date}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", type=str, required=True, help="Message to process")
    args = parser.parse_args()

    process_message(args.message)
