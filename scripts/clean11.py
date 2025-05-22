import re

# ---------------------------
def simplify_devanagari(text):
    cleaned = re.sub(r'[\u093E-\u094C\u0962\u0963]', '', text)  # Remove vowel signs like ा, ी etc.
    cleaned = re.sub(r'[\u0901-\u0903\u093C]', '', cleaned)    # Remove nasalization marks and nukta
    cleaned = re.sub(r'[^\u0900-\u097F]', '', cleaned)          # Remove non-Devanagari characters
    return cleaned

# ---------------------------
input_file = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/simplified_only_names2.txt"     # your input file path
output_file = "simplified_output.txt"  # output file path

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:

    for line in infile:
        line = line.strip()
        if not line:
            continue

        # Split word and count by '$'
        if '$' in line:
            word, count = line.split('$', 1)
            simplified_word = simplify_devanagari(word)
            outfile.write(f"{simplified_word}${count}\n")
        else:
            # If no $ separator, just simplify whole line and write
            simplified_word = simplify_devanagari(line)
            outfile.write(f"{simplified_word}\n")

print(f"Simplified file saved to: {output_file}")
