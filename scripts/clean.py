import json
import re

with open("../data/NewExport1.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

output_file = "place_names_cleaned.txt"

# ascii_only = re.compile(r"^[\x00-\x7F]+$")

names_set = set()

for feature in data.get("features", []):
    props = feature.get("properties", {})
    name = props.get("name")
    name = name.strip()
    names_set.add(name)

with open(output_file, "w", encoding="utf-8") as out:
    for name in sorted(names_set):
        out.write(f"{name}\n")

print(f"Extracted {len(names_set)} place names to {output_file}")
