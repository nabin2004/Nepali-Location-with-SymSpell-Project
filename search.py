from symspellpy import SymSpell, Verbosity
from itertools import islice

# Params
max_edit_distance = 3
prefix_length = 5
sym_spell = SymSpell(max_dictionary_edit_distance=max_edit_distance, prefix_length=prefix_length)

dictionary_path = "data/final_output_names.txt"
  
if not sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1, separator="$"):
    print("Failed to load dictionary")
    exit(1)
else:
    print("Dictionary loaded successfully.")

input_term = input("Enter a location search term: ").strip()

# Lookup similar terms 
suggestions = sym_spell.lookup(input_term, 
                               verbosity=Verbosity.ALL, 
                               max_edit_distance=max_edit_distance,
                               include_unknown=False)  

# Show results
print("Suggestions:")
if suggestions:
    for s in suggestions:
        print(f"{s.term} (edit distance: {s.distance}, frequency: {s.count})")
        break # Only show the first suggestion
else:
    print("No suggestions found.")
