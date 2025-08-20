import os
import requests

APP_ID = os.getenv("DISCORD_APP_ID")
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

url = f"https://discord.com/api/v10/applications/{APP_ID}/commands"

json = {
    "name": "ask",
    "description": "Pergunte sobre Pokémon competitivo",
    "options": [
        {
            "name": "question",
            "description": "Sua pergunta",
            "type": 3,
            "required": True
        }
    ]
}

headers = {
    "Authorization": f"Bot {BOT_TOKEN}"
}

r = requests.post(url, headers=headers, json=json)
print(r.status_code, r.text)
