import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_college_fee(college_name):
    # Google search se fees nikalne ka ek simple logic
    query = f"{college_name} annual fees structure 2025"
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        # Fees dhoondhne ke liye regex (₹ symbol ke saath numbers)
        fees_found = re.findall(r'₹\s?[0-9,.]+[LK]?', response.text)
        return fees_found[0] if fees_found else "Check Website"
    except:
        return "Contact College"

def update_db():
    # 1. Database read karein
    with open("database.js", "r", encoding='utf-8') as f:
        content = f.read()
        json_str = content.split("const colleges = ")[1].rstrip(";")
        colleges = json.loads(json_str)

    # 2. Sirf Fees column update karein
    for college in colleges:
        print(f"Scraping fees for {college['name']}...")
        college['fees'] = scrape_college_fee(college['name'])

    # 3. Wapas save karein
    with open("database.js", "w", encoding='utf-8') as f:
        f.write(f"const colleges = {json.dumps(colleges, indent=4)};")

if __name__ == "__main__":
    update_db()
