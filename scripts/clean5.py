input_path = "data/place_names_dictionary.txt"
output_path = "data/formatted_dictionary.csv"

with open(input_path, "r", encoding="utf-8") as infile, \
     open(output_path, "w", encoding="utf-8") as outfile:
    for line in infile:
        parts = line.strip().split('\t')
        if len(parts) >= 1:
            term = parts[0].strip().replace('"', '""')  # Escape any internal quotes
            outfile.write(f'"{term}",100\n')
