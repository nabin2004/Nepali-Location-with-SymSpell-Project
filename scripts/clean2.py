# create_dictionary.py
input_file = "data/place_names_cleaned.txt"
output_file = "data/place_names_dictionary.txt"

with open(input_file, "r", encoding="utf-8") as fin, \
     open(output_file, "w", encoding="utf-8") as fout:
    for line in fin:
        term = line.strip()
        if term:
            # frequency must be integer without quotes
            fout.write(f"{term}\t1\n")

print(f"Dictionary saved to {output_file}")
