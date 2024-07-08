import discord
import psutil
import time
from discord.ext import tasks
from pypresence import AioPresence

TOKEN = 'Your Discord Bot Token'
CLIENT_ID = 'Your Discord Application ID (Client)'
EXECUTABLE_NAME = r'C:\path\yourapplication.exe'


intents = discord.Intents.default()

class CustomClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.presence = AioPresence(CLIENT_ID)
        self.start_time = None
        self.playing_since = None

    async def setup_presence(self):
        await self.presence.connect()
        self.update_status.start()

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await self.setup_presence()

    @tasks.loop(seconds=10)
    async def update_status(self):
        if any(proc.name() == "yourapplication.exe" and proc.exe() == EXECUTABLE_NAME for proc in psutil.process_iter()):
            if self.start_time is None:
                self.start_time = int(time.time())
                self.playing_since = self.start_time

            current_time = int(time.time())
            elapsed_seconds = current_time - self.playing_since

            if elapsed_seconds <= 60:
                state_message = "Just started playing"
            else:
                elapsed_readable = self.format_time(elapsed_seconds)
                state_message = f"for {elapsed_readable}"

            await self.presence.update(
                state=state_message,
                small_image="YourRichPresenceAssets",
                small_text="Playing yourapplication", # unnecessary
                # start=self.start_time
            )
        else:
            self.start_time = None
            await self.presence.clear()

    def format_time(self, seconds):
        years = seconds // 31536000
        months = (seconds % 31536000) // 2592000
        weeks = (seconds % 2592000) // 604800
        days = (seconds % 604800) // 86400
        hours = (seconds % 86400) // 3600
        minutes = (seconds % 3600) // 60

        if years > 0:
            return f"{years} year" + ("s" if years > 1 else "")
        elif months > 0:
            return f"{months} month" + ("s" if months > 1 else "")
        elif weeks > 0:
            return f"{weeks} week" + ("s" if weeks > 1 else "")
        elif days > 0:
            return f"{days} day" + ("s" if days > 1 else "")
        elif hours > 0:
            return f"{hours} hour" + ("s" if hours > 1 else "")
        elif minutes > 0:
            return f"{minutes} minute" + ("s" if minutes > 1 else "")
        else:
            return "0 minutes"

def run_bot():
    client = CustomClient(intents=intents)
    client.run(TOKEN)

if __name__ == '__main__':
    run_bot()