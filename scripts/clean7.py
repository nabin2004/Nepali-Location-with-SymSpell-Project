import json

# Load Overpass Turbo GeoJSON file
with open("data/exporttest.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

features = data.get("features", [])

nepali_names = set()  # Use set to avoid duplicates

for feature in features:
    props = feature.get("properties", {})
    name_ne = props.get("name:ne")
    if name_ne:
        nepali_names.add(name_ne.strip())

# Sort the names
sorted_names = sorted(nepali_names)


for name in sorted_names:
    print(name)

# Save names to a file
with open("nepali_names.txt", "w", encoding="utf-8") as outfile:
    for name in sorted_names:
        outfile.write(name + "\n")
