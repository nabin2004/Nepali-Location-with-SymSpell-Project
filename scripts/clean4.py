import unicodedata

def is_valid_line(line):
    parts = line.strip().split('\t')
    return (
        len(parts) == 2 and 
        parts[1].isdigit()
    )

with open("data/place_names_dictionary.txt", "r", encoding="utf-8") as infile, \
     open("data/cleaned_dictionary.txt", "w", encoding="utf-8") as outfile:
    for line in infile:
        # Normalize and strip Unicode
        line = unicodedata.normalize("NFKC", line)
        if is_valid_line(line):
            outfile.write(line)
        else:
            print(f"Skipped invalid line: {line.strip()}")
