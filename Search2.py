import re
from symspellpy import SymSpell, Verbosity

# ---------------------------
# Simplification function
# ---------------------------
def simplify_devanagari(text):
    # Remove vowel signs (matras) and nasalization marks, nukta, etc.
    cleaned = re.sub(r'[\u093E-\u094C\u0962\u0963]', '', text)
    cleaned = re.sub(r'[\u0901-\u0903\u093C]', '', cleaned)
    cleaned = re.sub(r'[^\u0900-\u097F]', '', cleaned)
    return cleaned

# ---------------------------
# File paths
# ---------------------------
# symspell_dict_path = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/final_output_names.txt"
simplified_only_path = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/simplified_only_names.txt"
simplified_dict_path = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/simplified_dict.txt"

# ---------------------------
# Load SymSpell Dictionary
# ---------------------------
max_edit_distance = 3
prefix_length = 5
sym_spell = SymSpell(max_dictionary_edit_distance=max_edit_distance, prefix_length=prefix_length)

if not sym_spell.load_dictionary(simplified_only_path, term_index=0, count_index=1, separator="$"):
    print("Failed to load dictionary")
    exit(1)
else:
    print("Dictionary loaded successfully.")

# ---------------------------
# Load simplified dictionary as a lookup map
# ---------------------------
simplified_map = {}
with open(simplified_dict_path, "r", encoding="utf-8") as f:
    for line in f:
        if ":" not in line:
            continue
        parts = line.strip().strip(",").replace('"', '').split(":")
        if len(parts) == 2:
            orig, simp = parts[0].strip(), parts[1].strip()
            simplified_map[simp] = orig

# ---------------------------
# Input and process
# ---------------------------
input_term = input("Enter a location search term: ").strip()
simplified_input = simplify_devanagari(input_term)

# ---------------------------
# Lookup using simplified input
# ---------------------------
suggestions = sym_spell.lookup(simplified_input, 
                               verbosity=Verbosity.ALL, 
                               max_edit_distance=max_edit_distance,
                               include_unknown=False)

# ---------------------------
# Match to original
# ---------------------------
print("Suggestions:")
if suggestions:
    for s in suggestions:
        found_simplified = s.term
        if found_simplified in simplified_map:
            print(f"Original: {simplified_map[found_simplified]}")
            print(f"Simplified: {found_simplified}")
        else:
            print(f"Simplified: {found_simplified} (Original not found in simplified_dict.txt)")
        break
else:
    print("No suggestions found.")
