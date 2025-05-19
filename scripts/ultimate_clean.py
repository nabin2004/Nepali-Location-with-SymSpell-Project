import re

def simplify_devanagari(text):
    # Remove vowel signs (matras) and nasalization marks, nukta, etc.
    cleaned = re.sub(r'[\u093E-\u094C\u0962\u0963]', '', text)
    cleaned = re.sub(r'[\u0901-\u0903\u093C]', '', cleaned)
    # Keep only Devanagari characters
    cleaned = re.sub(r'[^\u0900-\u097F]', '', cleaned)
    return cleaned

input_path = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/final_output_names.txt"
output_path = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/simplified_dict.txt"

pairs = []

with open(input_path, "r", encoding="utf-8") as infile:
    for line in infile:
        if "$" not in line:
            continue
        original = line.split("$")[0].strip()
        simplified = simplify_devanagari(original)
        if simplified and simplified != original:
            pairs.append((original, simplified))

with open(output_path, "w", encoding="utf-8") as outfile:
    outfile.write("{\n")
    for orig, simp in pairs:
        outfile.write(f'\t"{orig}": "{simp}",\n')
    outfile.write("}\n")

print("Dictionary pairs written to:", output_path)
