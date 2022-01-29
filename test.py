from discord import Client, Message, Member
from os import environ
import logging

logging.basicConfig(level=logging.INFO)

user_id = int(environ.get("BAN_USER_ID", "735612271425880156"))
ban_reason = environ.get("BAN_REASON", "mamam for ritot")
token = environ.get("BOT_TOKEN")

bot = Client()

@bot.event
async def on_message(message: Member):
    if message.author.id == user_id:
        message.author.ban(reason=ban_reason)

@bot.event
async def on_voice_state_update(member: Member):
    if member.id == user_id:
        member.ban(reason=ban_reason)

bot.run(token)