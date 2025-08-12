import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

async def main():
    api_id = 24742209  # আপনার API_ID এখানে বসান
    api_hash = 'c0694019a65cc128f92fe03df8cb4bd0'  # আপনার API_HASH এখানে বসান

    async with TelegramClient(StringSession(), api_id, api_hash) as client:
        print("\n\nCopy this STRING_SESSION value and keep it secret:\n")
        print(client.session.save())
        print("\n\nNow you can use this STRING_SESSION as an environment variable.\n")

if __name__ == "__main__":
    asyncio.run(main())
