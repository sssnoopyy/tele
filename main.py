from telethon import TelegramClient, events


api_id = 29313429
api_hash = '352bbf38fc601e478ee87ce924eeec3e'
phone_number = '3023426435'


client = TelegramClient('self_bot', api_id, api_hash)


@client.on(events.NewMessage)
async def handle_message(event):
    chat = await event.get_chat()
    sender = await event.get_sender()
    if event.is_private and sender.bot:
        if event.raw_text.startswith('.test'):
            await event.respond("test")


client.start(phone_number)
client.run_until_disconnected()
