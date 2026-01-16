from telethon import TelegramClient
import json

api_id = 39533424
api_hash = "2ddb7ea287d91744c2ae2aab318c0bf6"

client = TelegramClient("test_session",api_id,api_hash)

async def channel_collector(channel, limit=50):
    await client.start()

    data = []

    async for message in client.iter_messages(channel, limit=limit):
        data.append({
            "ID":message.id,
            "DATE":message.date.isoformat() if message.date else None,
            "TEXT":message.text
        })

    with open("single_channel_test.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

