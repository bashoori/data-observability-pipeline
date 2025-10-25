import requests
import json
import os


def fetch_data():
    """
    Fetch product data directly from Shopify JSON endpoint (Natural Factors).
    """
    os.makedirs("data/tmp", exist_ok=True)
    file_path = os.path.join("data/tmp", "raw_api_data.json")

    url = "https://ca.naturalfactors.com/collections/all-products/products.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        products = data.get("products", [])
        print(f"✅ Successfully fetched {len(products)} products from Shopify JSON.")
    except Exception as e:
        print(f"❌ Failed to fetch products ({e})")
        products = []

    with open(file_path, "w") as f:
        json.dump(products, f, indent=2)

    print(f"✅ Saved {len(products)} records to {file_path}")


