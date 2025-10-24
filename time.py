import asyncio
from datetime import datetime
import pytz
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest

# ======= ضع هنا بياناتك مباشرة =======
API_ID = 17400306
API_HASH = "fbc295e7bd64178a0755626eff0682de"
SESSION_STRING = "1ApWapzMBuwI4qsOmVZqgMOZNwSAadZ5MC87DA6em0V7Npke8HbolshjRky7Br7kphiypLstcg5D_EWqsc1fx48Tnjr5Un6SM5jiVgZNj6DtNc8CIQEXOM-fu_4GbYR02p1HuqUP0ixLXT-6DrDC3MZvcaaOmhAHKijuiJcur3htLoAejw9d8vduNG7ZlXG5PREL7Fxl9igFHvV9n9169ZS7fWhDfDEK5WfyW0pkczzRRo2iP-tqFVwtongGXIFG4avO7tlFjozT_8rwb0gAuorVyvGgMRIQ0KCMTmHJY9QdlWjoZ2oy_vopP7SPuUr1fxb06qWtycXSqMxHlo4JmKbnSRmE32PI="
# =======================================

TZ = "Asia/Baghdad"

style = str.maketrans("0123456789", "０１２۳４５６７８９")
def fancy_time(t: str) -> str:
    return t.translate(style)

async def main():
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    await client.start()

    me = await client.get_me()
    print(f"شغال ✅ بحساب: {me.first_name}")

    while True:
        now = datetime.now(pytz.timezone(TZ)).strftime("%H:%M")
        fancy = fancy_time(now)
        try:
            await client(UpdateProfileRequest(
                last_name=f"⏰ {fancy}"
            ))
            print("تم تحديث:", fancy)
        except Exception as e:
            print("خطأ:", e)

        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
