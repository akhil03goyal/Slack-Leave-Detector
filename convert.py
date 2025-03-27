import spacy
import json
import re
from datetime import datetime, timedelta

# Load blank spaCy model
nlp = spacy.blank("en")

# Define relative date replacements
def normalize_dates(text):
    today = datetime.today()
    
    # Define correct date replacements
    def get_next_weekday(weekday):
        days_ahead = (weekday - today.weekday() + 7) % 7
        return (today + timedelta(days=days_ahead)).strftime("%d-%m-%Y")

    replacements = {
        "today": today.strftime("%d-%m-%Y"),
        "tomorrow": (today + timedelta(days=1)).strftime("%d-%m-%Y"),
        "next Friday": get_next_weekday(4),  # 4 represents Friday
    }

    # Adjust offsets correctly
    replaced_offsets = {}
    for word, new_value in replacements.items():
        pattern = r"\b" + re.escape(word) + r"\b"
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        
        for match in matches:
            replaced_offsets[match.group()] = new_value
            text = text[:match.start()] + new_value + text[match.end():]

    return text, replaced_offsets

# Load training data
with open("training_data.json", "r") as f:
    training_data = json.load(f)

cleaned_data = []

for text, annotations in training_data:
    original_text = text
    modified_text, replaced_offsets = normalize_dates(text)  # Normalize dates

    print(f"\n🔍 Original: {original_text}")
    print(f"✅ Processed: {modified_text}")

    # Adjust entity offsets
    new_entities = []
    for start, end, label in annotations["entities"]:
        entity_text = original_text[start:end]

        # Check if entity_text was modified
        if entity_text in replaced_offsets:
            new_entity_text = replaced_offsets[entity_text]
            new_start = modified_text.find(new_entity_text)
        else:
            new_start = modified_text.find(entity_text)

        # If entity still not found, skip it
        if new_start == -1:
            print(f"⚠️ Skipping entity '{entity_text}' ({label}) - Not found in modified text.")
            continue

        new_end = new_start + len(new_entity_text)
        new_entities.append([new_start, new_end, label])

    # Store cleaned entry
    cleaned_data.append([modified_text, {"entities": new_entities}])

# Save cleaned data
with open("cleaned_training_data.json", "w") as f:
    json.dump(cleaned_data, f, indent=4)

print("\n✅ Training data successfully cleaned and saved!")
