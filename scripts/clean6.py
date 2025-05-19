input_path = "data/place_names_dictionary.txt"
output_path = "data/formatted_dictionary.txt"

with open(input_path, "r", encoding="utf-8") as infile, \
     open(output_path, "w", encoding="utf-8") as outfile:
    for line in infile:
        parts = line.strip().split('\t')
        if len(parts) >= 1:
            term = parts[0].strip()
            if term:
                # Use fixed frequency 100 or use parts[1] if you want original frequency
                frequency = "100"
                # Write as "term$frequency"
                outfile.write(f"{term}${frequency}\n")
