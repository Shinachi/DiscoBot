import discord

client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after):
  if before.channel != after.channel:
    botRoom = client.get_channel(975394412664344620)

    announceChannelIds = [975394412664344621, 979621751963156520]

    if before.channel is not None and before.channel.id in announceChannelIds:
      await botRoom.send("**" + before.channel.name + "** から、__" + member.name + "__  が抜けたよ")
    if after.channel is not None and after.channel.id in announceChannelIds:
        await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加したよ")

client.run("OTc5MjYyODE5MTU5NjQyMTIy.Gcbwt7._NGRaYCNY-Y4XUpxXxZY6_oOHXJuaWjM9MyyHw")