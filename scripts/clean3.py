



with open("data/place_names_dictionary.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        parts = line.rstrip('\r\n').split('\t')
        if len(parts) != 2:
            print(f"Line {i} malformed: {repr(line)}")
        else:
            term, freq = parts
            if not freq.isdigit():
                print(f"Line {i} frequency invalid: '{freq}' (type: {type(freq)})")