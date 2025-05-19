input_path = "../nepali_names.txt"
output_path = "output_names.txt"

with open(input_path, "r", encoding="utf-8") as infile, \
     open(output_path, "w", encoding="utf-8") as outfile:
    for line in infile:
        name = line.strip()
        if name:  # skip empty lines
            outfile.write(f"{name}$100\n")
