import json

TRAINING_DATA = [
    ("I am taking a leave today.", {"entities": [(17, 22, "LEAVE_TYPE"), (23, 28, "DATE")]}),
    ("I am sick and won't be working.", {"entities": [(5, 9, "LEAVE_TYPE")]}),  # Fixed label
    ("On vacation tomorrow.", {"entities": [(3, 11, "LEAVE_TYPE"), (12, 20, "DATE")]}),
    ("I have an emergency and can't come today.", {"entities": [(9, 18, "LEAVE_TYPE"), (35, 40, "DATE")]}),
]

with open("training_data.json", "w") as f:
    json.dump(TRAINING_DATA, f, indent=4)

print("✅ Training data saved successfully!")
