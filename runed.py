import re
from symspellpy import SymSpell, Verbosity
from nepali_stemmer.stemmer import NepStemmer
from itertools import product
from typing import List, Tuple, Dict, Set

def simplify_devanagari(text: str) -> str:
    """Simplify Devanagari text by removing diacritics and non-Devanagari characters."""
    cleaned = re.sub(r'[\u093E-\u094C\u0962\u0963]', '', text)
    cleaned = re.sub(r'[\u0901-\u0903\u093C]', '', cleaned)
    cleaned = re.sub(r'[^\u0900-\u097F]', '', cleaned)
    return cleaned

def load_vocab(filepath: str) -> Set[str]:
    """Load base vocabulary from file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}

def load_simplified_map(filepath: str) -> Dict[str, str]:
    """Load simplified to original word map."""
    simplified_map = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if ":" not in line:
                continue
            parts = line.strip().strip(",").replace('"', '').split(":")
            if len(parts) == 2:
                orig, simp = parts[0].strip(), parts[1].strip()
                simplified_map[simp] = orig
    return simplified_map

def init_spellchecker(dict_path: str, max_edit_distance: int = 2, prefix_length: int = 3) -> SymSpell:
    """Initialize SymSpell with the given dictionary file."""
    sym_spell = SymSpell(max_dictionary_edit_distance=max_edit_distance, prefix_length=prefix_length)
    if not sym_spell.load_dictionary(dict_path, term_index=0, count_index=1, separator="$"):
        raise ValueError("Failed to load dictionary from: " + dict_path)
    return sym_spell

def correct_sentence(
    sentence: str,
    sym_spell: SymSpell,
    nepstem: NepStemmer,
    simplified_map: Dict[str, str],
    vocab: Set[str],
    top_k: int = 3
) -> List[str]:
    """Return all top-k corrected sentence variants."""
    words = sentence.split()
    sentence_options = []

    for word in words:
        if word in vocab:
            sentence_options.append([word])
            continue

        stemmed_tokens = nepstem.stem(word).split()
        base_stem = stemmed_tokens[0]
        simplified = simplify_devanagari(base_stem)

        suggestions = sym_spell.lookup(
            simplified,
            verbosity=Verbosity.ALL,
            max_edit_distance=sym_spell._max_dictionary_edit_distance,
            include_unknown=False
        )

        correction_list = []
        if suggestions:
            for suggestion in suggestions[:top_k]:
                corrected_base = simplified_map.get(suggestion.term, base_stem)
                if len(stemmed_tokens) > 1:
                    full_word = corrected_base + ''.join(stemmed_tokens[1:])
                else:
                    full_word = corrected_base
                correction_list.append(full_word)
        else:
            correction_list = [word]

        sentence_options.append(correction_list)

    corrected_variants = [' '.join(variant) for variant in product(*sentence_options)]
    return corrected_variants

def main():
    # Paths 
    simplified_only_path = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/simplified_only_names2.txt"
    simplified_dict_path = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/simplified_dict.txt"
    vocab_path = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/vocab.txt"

    # Initializing components
    sym_spell = init_spellchecker(simplified_only_path)
    simplified_map = load_simplified_map(simplified_dict_path)
    vocab = load_vocab(vocab_path)
    nepstem = NepStemmer()

    # Example sentences
    nepali_sentences = [
        "भतपरको  जिज्ञासु वातावरणले धेरै पर्यटकलाई आकर्षित गर्छ।",
        "ललतपुर प्राचीन मूर्तिकला र वास्तुकलाको केन्द्र हो।",
    ]

    for sentence in nepali_sentences:
        corrected_variants = correct_sentence(sentence, sym_spell, nepstem, simplified_map, vocab, top_k=3)
        print(f"Original: {sentence}")
        print(f"Generated {len(corrected_variants)} variants:\n")
        for i, variant in enumerate(corrected_variants):
            print(f"[{i+1}] {variant}")
        print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()