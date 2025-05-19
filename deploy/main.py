import re
import gradio as gr
from symspellpy import SymSpell, Verbosity

# ---------------------------
# Simplification function
# ---------------------------
def simplify_devanagari(text):
    cleaned = re.sub(r'[\u093E-\u094C\u0962\u0963]', '', text)
    cleaned = re.sub(r'[\u0901-\u0903\u093C]', '', cleaned)
    cleaned = re.sub(r'[^\u0900-\u097F]', '', cleaned)
    return cleaned

# ---------------------------
# File paths
# ---------------------------
simplified_only_path = "./data/simplified_only_names.txt"
simplified_dict_path = "./data/simplified_dict.txt"

# ---------------------------
# Load simplified dictionary
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
# Main Gradio function
# ---------------------------
def lookup_location(input_term, max_edit_distance, prefix_length):
    sym_spell = SymSpell(max_dictionary_edit_distance=max_edit_distance, prefix_length=prefix_length)

    if not sym_spell.load_dictionary(simplified_only_path, term_index=0, count_index=1, separator="$"):
        return "Failed to load dictionary."

    simplified_input = simplify_devanagari(input_term)
    
    suggestions = sym_spell.lookup(
        simplified_input,
        verbosity=Verbosity.ALL,
        max_edit_distance=max_edit_distance,
        include_unknown=False
    )

    if suggestions:
        for s in suggestions:
            found_simplified = s.term
            original = simplified_map.get(found_simplified, "Not found in dictionary.")
            return f"Input: {input_term}\nSimplified: {found_simplified}\nOriginal: {original}"
    else:
        return f"No suggestions found for: {input_term}"

# ---------------------------
# Gradio UI
# ---------------------------
iface = gr.Interface(
    fn=lookup_location,
    inputs=[
        gr.Textbox(label="Enter Nepali location name"),
        gr.Slider(1, 5, value=3, step=1, label="Max Edit Distance"),
        gr.Slider(1, 10, value=5, step=1, label="Prefix Length")
    ],
    outputs=gr.Textbox(label="Result"),
    title="Nepali Fuzzy Location Lookup",
    description="Uses regex simplification, SymSpell fuzzy match, and maps back to original name. Adjust max edit distance and prefix length.",
    examples=[
        ["काठमाडौँ", 3, 5],
        ["सुकेधारा", 3, 5],
        ["गोंगबु", 3, 5],
        ["माइतीघर", 2, 5],
        ["कलंकी", 2, 5],
    ]
)

iface.launch(share=True)
