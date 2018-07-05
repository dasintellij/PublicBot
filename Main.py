import discord
import Secret

client = discord.Client()
prefix = "BOTPREFIX"
serverid = "ServerID"
reportchannelid = "REPORTCHANNELID"
rechte = ['CLIENT ID 1',
		  'CLIENT ID 2',
		  'CLIENT ID 3',]


@client.event
async def on_ready():
    print("Bot is online")

@client.event
async def on_message(message):

    if message.content == prefix + "bot":
        await client.send_message(message.channel, "Der Bot wurde von DasIntellij#2991 Programmiert.")

    if message.content.lower().startswith(prefix + 'report'):
        report = message.content[len(prefix + 'report'):].strip()
        msg = "`Neuer Report:`\n" + "**"+ report + "**"
        server = client.get_server(serverid)
        await client.send_message(discord.Object(reportchannelid), msg)
        await client.delete_message(message)
        await client.send_message(message.channel, "**Report sent.**")

    if message.content.lower().startswith(prefix + 'ban') and rechte.__contains__(message.author.id):
        user = message.mentions[0]
        await client.ban(user)
        await client.send_message(message.channel, 'User gebannt.')
		
    if message.content.lower().startswith(prefix + 'kick') and rechte.__contains__(message.author.id):
        user = message.mentions[0]
        await client.kick(user)
        await client.send_message(message.channel, 'User gekickt.')

client.run(Secret.token)
