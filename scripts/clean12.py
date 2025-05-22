import re
import json

def simplify_devanagari(text):
    cleaned = re.sub(r'[\u093E-\u094C\u0962\u0963]', '', text)  # Remove vowel signs and special marks
    cleaned = re.sub(r'[\u0901-\u0903\u093C]', '', cleaned)     # Remove nasalization and nukta
    cleaned = re.sub(r'[^\u0900-\u097F]', '', cleaned)          # Keep only Devanagari unicode block
    return cleaned

input_lines = [
    "भक्तपुर$100",
    "ललितपुर$100",
    "पोखरा$100",
    "विराटनगर$100",
    "धरान$100",
    "बुटवल$100",
    "धनगढी$100",
    "नेपालगंज$100",
    "जनकपुर$100",
    "बिरगंज$100",
    "सर्लाही$100",
    "मोरङ$100",
    "रुपन्देही$100",
    "सिन्धुपाल्चोक$100",
    "धादिङ$100",
    "रसुवा$100",
    "सिन्धुली$100",
    "सुकेकोट$100",
    "सुकेटार$100",
    "सुकेधारा$100",
    "पशुपतिनाथ$100",
    "सिंहदरबार$100",
    "नारायणहिटी$100",
    "त्रिपुरेश्वर$100",
    "बौद्ध$100"
]

mapping = {}

for line in input_lines:
    if '$' not in line:
        continue
    original, _ = line.split('$', 1)
    simplified = simplify_devanagari(original)
    mapping[original] = simplified

# Save or print the mapping
output_file = "simplified_mapping.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(mapping, f, ensure_ascii=False, indent=4)

print(f"Simplified mapping saved to {output_file}")
print(mapping)
