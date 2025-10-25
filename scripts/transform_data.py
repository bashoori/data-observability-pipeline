import json, os

def transform_data():
    with open("/tmp/raw_api_data.json") as f:
        records = json.load(f)

    cleaned = [
        {
            "id": r["id"],
            "title": r["title"].strip(),
            "category": r["category"],
            "price": r["price"],
            "rating": r["rating"]["rate"]
        }
        for r in records
    ]

    with open("/tmp/clean_data.json", "w") as f:
        json.dump(cleaned, f)

    print(f"✅ Transformed {len(cleaned)} records")
