import json

input_file = "/home/nabin/Desktop/Allprojects/SymSpellProj/data/simplified_dict2.txt"
output_file = "output.json"

# Load existing dictionary from the file
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# If you want to just print it nicely:
print(json.dumps(data, ensure_ascii=False, indent=4))

# Or write it back to another file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Data loaded from {input_file} and saved to {output_file}")
