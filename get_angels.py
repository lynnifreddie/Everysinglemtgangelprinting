import os
import subprocess
import time
import pandas as pd
import requests

print("🧙 Connecting to Scryfall API...")

# 1. Build the Scryfall search query
url = "https://api.scryfall.com/cards/search"
params = {
    "q": "type:angel is:paper",
    "unique": "prints",
    "include_multilingual": "true"
}

all_cards = []
has_more = True

# 2. Page through Scryfall's database to capture all 1,450+ variants
while has_more:
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"❌ Error fetching data: {response.status_code}")
        break
        
    data = response.json()
    all_cards.extend(data.get("data", []))
    
    has_more = data.get("has_more", False)
    if has_more:
        url = data.get("next_page")
        params = None  # Next page URL already includes the parameters
        time.sleep(0.1)  # Polite pause so we don't overwhelm Scryfall's server

print(f"✨ Successfully pulled {len(all_cards)} global Angel printings!")

# 3. Process data into a clean structure
processed_cards = []
for card in all_cards:
    processed_cards.append({
        "Name": card.get("name"),
        "Printed Name": card.get("printed_name", card.get("name")),
        "Language": card.get("lang").upper(),
        "Set Code": card.get("set").upper(),
        "Set Name": card.get("set_name"),
        "Collector Number": card.get("collector_number"),
        "Rarity": card.get("rarity").capitalize(),
        "Scryfall ID": card.get("id")
    })

# 4. Save directly into your master Excel spreadsheet
df = pd.DataFrame(processed_cards)
excel_filename = "all_mtg_angels.xlsx"
df.to_excel(excel_filename, index=False)
print(f"📊 Saved master data to {excel_filename}!")

# 5. AUTOMATIC HANDSHAKE: Trigger your gorgeous custom angel wing popup!
script_dir = os.path.dirname(os.path.abspath(__file__))
popup_path = os.path.join(script_dir, "run_popup.py")

if os.path.exists(popup_path):
    print("🚀 Launching celebration window...")
    subprocess.run(["python", popup_path])
else:
    print("⚠️ run_popup.py not found in the same folder, skipping popup.")