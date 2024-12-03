import discord
from discord.ext import commands
import ipinfo

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'
# Replace 'YOUR_IPINFO_TOKEN' with your actual ipinfo token
IPINFO_TOKEN = 'YOUR_IPINFO_TOKEN'

# Initialize the bot
bot = commands.Bot(command_prefix='!')

# Initialize the ipinfo handler
handler = ipinfo.getHandler(IPINFO_TOKEN)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ipinfo(ctx, ip: str):
    try:
        details = handler.getDetails(ip)
        response = (
            f"IP Address: {details.ip}\n"
            f"City: {details.city}\n"
            f"Region: {details.region}\n"
            f"Country: {details.country}\n"
            f"Location: {details.loc}\n"
            f"Organization: {details.org}\n"
            f"Postal: {details.postal}\n"
            f"Timezone: {details.timezone}\n"
        )
    except Exception as e:
        response = f"Error: {str(e)}"
    
    await ctx.send(response)

bot.run(BOT_TOKEN)