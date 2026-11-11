import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import database

load_dotenv()
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("Discord token tidak ditemukan")

intents = discord.Intents.default()
intents.message_content = True

class TaskManagerBot(commands.Bot):
    async def setup_hook(self):
        database.init_db()
        await self.load_extension("commands")

bot = TaskManagerBot(
    command_prefix = "!",
    intents = intents
)    

@bot.event
async def on_ready():
    print(f"Bot {bot.user} sudah online!")

bot.run(TOKEN)