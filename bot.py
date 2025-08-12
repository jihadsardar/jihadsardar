from telethon import TelegramClient, events, Button
import re
# ====== SESSION 1 CONFIG ======
api_id_1 = 24742209
api_hash_1 = 'c0694019a65cc128f92fe03df8cb4bd0'
file_source_1 = -1002516977814  # Source Group
file_forward_to_1 = -1002546523324  # Target Channel
your_group_link_1 = "https://t.me/otphostgroup"
# ====== SESSION 2 CONFIG ======
api_id_2 = 24742209
api_hash_2 = 'c0694019a65cc128f92fe03df8cb4bd0'
file_source_2 = -1002506219108  # Source Group
file_forward_to_2 = -1002546523324  # Target Channel
your_group_link_2 = "https://t.me/otphostgroup"
old_username = "@Rifat103300"
new_username = "@Jihadsardar90"
# ====== SESSION 3 CONFIG ======
api_id_3 = 24742209
api_hash_3 = 'c0694019a65cc128f92fe03df8cb4bd0'
file_source_3 = -1002767619355  # Source Group 
file_forward_to_3 = -1002546523324  # Target Channel
your_group_link_3 = "https://t.me/otphostgroup"
# ====== CLIENTS ======
client1 = TelegramClient('file_forward_session_1', api_id_1, api_hash_1)
client2 = TelegramClient('file_forward_session_2', api_id_2, api_hash_2)
client3 = TelegramClient('file_forward_session_3', api_id_3, api_hash_3)
# ====== SESSION 1 FILE FORWARDING ======
@client1.on(events.NewMessage(chats=file_source_1))
async def forward_file_1(event):
    if event.file or event.raw_text:
        caption = event.raw_text or ""
        # OTP code check for facebook only
        if re.search(r'\b\d{4,8}\b', caption.lower()) and "facebook" in caption.lower():
            # If contains facebook OTP code, forward message as text (optional, can be file + text)
            await client1.send_message(
                file_forward_to_1,
                message=caption,
                buttons=[Button.url("🔐 Join Group", your_group_link_1)]
            )
        elif event.file:
            # Normal file forwarding with cleaned caption
            lines = caption.splitlines()
            cleaned_lines = [
                re.sub(r'(@\w+|https?://t\.me/\S+|t\.me/\S+|telegram\.me/\S+)', '', line)
                for line in lines
            ]
            cleaned_caption = "\n".join(cleaned_lines).strip()
            await client1.send_file(
                file_forward_to_1,
                file=event.media,
                caption=cleaned_caption,
                buttons=[Button.url("🔐 Join Group", your_group_link_1)]
            )
# ====== SESSION 2 FILE FORWARDING ======
@client2.on(events.NewMessage(chats=file_source_2))
async def forward_file_2(event):
    if event.file or event.raw_text:
        caption = event.raw_text or ""
        # Replace old username with new username
        caption = caption.replace(old_username, new_username)
        if re.search(r'\b\d{4,8}\b', caption.lower()) and "facebook" in caption.lower():
            await client2.send_message(
                file_forward_to_2,
                message=caption,
                buttons=[Button.url("🔐 Join Group", your_group_link_2)]
            )
        elif event.file:
            lines = caption.splitlines()
            cleaned_lines = [
                re.sub(r'(@\w+|https?://t\.me/\S+|t\.me/\S+|telegram\.me/\S+)', '', line)
                for line in lines
            ]
            cleaned_caption = "\n".join(cleaned_lines).strip()
            await client2.send_file(
                file_forward_to_2,
                file=event.media,
                caption=cleaned_caption,
                buttons=[Button.url("🔐 Join Group", your_group_link_2)]
            )
# ====== SESSION 3 FILE FORWARDING ======
@client3.on(events.NewMessage(chats=file_source_3))
async def forward_file_3(event):
    if event.file or event.raw_text:
        caption = event.raw_text or ""
        if re.search(r'\b\d{4,8}\b', caption.lower()) and "facebook" in caption.lower():
            await client3.send_message(
                file_forward_to_3,
                message=caption,
                buttons=[Button.url("🔐 Join Group", your_group_link_3)]
            )
        elif event.file:
            lines = caption.splitlines()
            cleaned_lines = [
                re.sub(r'(@\w+|https?://t\.me/\S+|t\.me/\S+|telegram\.me/\S+)', '', line)
                for line in lines
            ]
            cleaned_caption = "\n".join(cleaned_lines).strip()
            await client3.send_file(
                file_forward_to_3,
                file=event.media,
                caption=cleaned_caption,
                buttons=[Button.url("🔐 Join Group", your_group_link_3)]
            )
print("✅ File forwarding systems running (Facebook OTP included as text)...")
client1.start()
client2.start()
client3.start()
client1.run_until_disconnected()
client2.run_until_disconnected()
client3.run_until_disconnected()
