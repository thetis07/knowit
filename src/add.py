import json

dt = "dictionary.json"

def add(key, value, level):
    with open(dt, "r") as f:
        source = json.load(f)

    level_dict = source.get(level)
    level_dict[key] = value

    with open(dt, "w") as f:
        json.dump(source, f, ensure_ascii=False, indent=4)

    print(f"basarıyla eklendi! {key}, {value} demek")