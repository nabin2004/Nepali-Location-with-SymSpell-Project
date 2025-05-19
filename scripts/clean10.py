import re

def simplify_devanagari(text):
    # Remove vowel signs (matras) and nasalization marks, nukta, etc.
    cleaned = re.sub(r'[\u093E-\u094C\u0962\u0963]', '', text)
    cleaned = re.sub(r'[\u0901-\u0903\u093C]', '', cleaned)
    cleaned = re.sub(r'[^\u0900-\u097F]', '', cleaned)
    return cleaned

# Input file with original words
input_path = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/final_output_names.txt"

# Output file with simplified words + $100
output_path = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/simplified_only_names.txt"

simplified_set = set()

with open(input_path, "r", encoding="utf-8") as infile:
    for line in infile:
        if "$" not in line:
            continue
        original = line.split("$")[0].strip()
        simplified = simplify_devanagari(original)
        if simplified:
            simplified_set.add(simplified)

# Write simplified lines with $100
with open(output_path, "w", encoding="utf-8") as outfile:
    for word in sorted(simplified_set):
        outfile.write(f"{word}$100\n")

print("Simplified names written to:", output_path)
