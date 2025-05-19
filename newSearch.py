from symspellpy import SymSpell, Verbosity

# Parameters
max_edit_distance = 4
prefix_length = 5
sym_spell = SymSpell(max_dictionary_edit_distance=max_edit_distance, prefix_length=prefix_length)

# Load dictionary
dictionary_path = "data/test.txt"
if not sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1):
    print("Failed to load dictionary")
    exit(1)

# Input sentence
text = "मेरो घर Kathman मा हो मेरो घर Ktm हो"

# Tokenize by whitespace
tokens = text.split()

corrected_tokens = []
for token in tokens:
    if token in sym_spell.words:
        corrected_tokens.append(token)
    else:
        # Lookup suggestions
        suggestions = sym_spell.lookup(token,
                                       verbosity=Verbosity.CLOSEST,
                                       max_edit_distance=max_edit_distance,
                                       include_unknown=False)
        if suggestions:
            # Use the best suggestion
            corrected_tokens.append(suggestions[0].term)
        else:
            corrected_tokens.append(token)  # Keep original if no match

# Reconstruct the sentence
corrected_text = " ".join(corrected_tokens)
print("Corrected:", corrected_text)
