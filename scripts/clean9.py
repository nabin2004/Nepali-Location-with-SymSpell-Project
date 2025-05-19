from collections import Counter

# File paths
input_path = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/final_output_names.txt"
output_path = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/unigram_counts.txt"

# Store all unigrams
unigram_counter = Counter()

with open(input_path, "r", encoding="utf-8") as infile:
    for line in infile:
        if "$" not in line:
            continue
        word = line.split("$")[0].strip()
        unique_chars = set(word)  # optional: use set() to count each char once per line
        unigram_counter.update(unique_chars)

# Write unigram counts to file
with open(output_path, "w", encoding="utf-8") as outfile:
    for char, count in unigram_counter.most_common():
        outfile.write(f"{char}${count}\n")

print("Unigram count written to:", output_path)
