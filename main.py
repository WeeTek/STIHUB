import asyncio

import discord
from discord.ext import commands
from discord.utils import get
import os
import mysql.connector
import time


import youtube_dl
import asyncio


musics = {}
ytdl = youtube_dl.YoutubeDL()


intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

conn = mysql.connector.connect(host="136.243.72.220",
                               user="u3152_26puVHlJVI", password="FcJ2h4j4M.bhXIMEs@^PT82E", database="s3152_account")

cursor = conn.cursor()


@bot.event
async def on_ready():
    print("Bot pret")
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(" :😍: Deutsch qualitat"))
    file_name = 'welcome.txt'
    file_role = "role.txt"
    f = open(file_role, 'a')
    f = open(file_name, 'a')
    f.close()


@bot.event
async def on_ready():
    print("Ready")


class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]


@bot.command()
async def leave(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []


@bot.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()


@bot.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()


@bot.command()
async def skip(ctx):
    client = ctx.guild.voice_client
    client.stop()


def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
                                                                 ,
                                                                 before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)

    client.play(source, after=next)


@bot.command()
async def play(ctx, url):
    print("play")
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        await ctx.send(f"Je lance : {video.url}")
        play_song(client, musics[ctx.guild], video)




@bot.command()
async def welcome(ctx):
    channel = ctx.channel.id
    file_name = "welcome.txt"
    if os.stat(file_name).st_size == 0:
        f = open(file_name, 'w')
        f.write(str(channel))
        f.close()
        print(channel)

        embed = discord.Embed(title="**Changement salon accueil**", description="Le salon de bienvenue à été changé",
                              color=0xfa8072)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/271"
                                "/door_1f6aa.png")
        embed.add_field(name="Nouveau Channel arrivant", value="les nouveaux arrivant apparaitront ici", inline=True)
        await ctx.send(embed=embed)
    else:
        f = open(file_name, 'w')
        f.write(str(channel))
        f.close()
        embed = discord.Embed(title="**Changement salon accueil**", description="Le salon de bienvenue à été changé",
                              color=0xfa8072)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/271"
                                "/door_1f6aa.png")
        embed.add_field(name="Nouveau Channel arrivant", value="les nouveaux arrivant apparaitront ici", inline=True)
        await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def rankup(ctx, role: discord.guild.Role, *, desc=None):
    embed = discord.Embed(title="**Donne le role **" + role.name, description=desc,
                          color=0xfa8072)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="Clique", value="⬇️⬇️⬇⬇️️")
    message = await ctx.send(embed=embed)
    name = role.name
    msg_id = message.id
    query = "INSERT INTO `Role`(`role_name`, `message_id`) VALUES (%s, %s)"
    insert_tuple = (name, str(msg_id))
    cursor.execute(query, insert_tuple)
    await message.add_reaction("✅")


@bot.command()
@commands.has_permissions(administrator=True)
async def goulag(ctx, member: discord.Member, reason=None, ti=None):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name="goulag")
    if reason is None:
        reason = "non respect des règles"
    if reason is not None:
        reason = reason
    if ti is None:
        await member.add_roles(role)
        await member.send("Tu as été envoyé au goulag pour " + reason)
    if ti is not None:
        if str(ti).endswith("d"):
            res = ti[:-1]
            await member.send("Tu as été envoyé au goulag pendant " + res + " jours pour " + reason)
            await member.add_roles(role)
            await asyncio.sleep(int(res) * 86400)
            await member.remove_roles(role)
    if ti is not None:
        if str(ti).endswith("h"):
            res = ti[:-1]
            await member.send("Tu as été envoyé au goulag  pendant " + res + " heures pour " + reason)
            await member.add_roles(role)
            await asyncio.sleep(int(res) * 3600)
            await member.remove_roles(role)


@bot.command()
@commands.has_permissions(administrator=True)
async def att_goulag(ctx):
    channel = ctx.channel.id
    file_name = "goulag.txt"
    if os.stat(file_name).st_size == 0:
        f = open(file_name, 'w')
        f.write(str(channel))
        f.close()

        embed = discord.Embed(title="**Changement du salon goulag**", description="C'est ici le goulag maintenant",
                              color=0xfa8072)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(
            url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQZtSN-9fn7Cig3DK-v1naUBVC_dZ4PfkOHZ7SlLkJZ3mvoSektLiHTHdw8Ug1JVnCJaQ&usqp=CAU")
        embed.add_field(name="Ceux qui ont fait de la merde finisse ici", value="les connards terminent ici",
                        inline=True)
        await ctx.send(embed=embed)
    else:
        f = open(file_name, 'w')
        f.write(str(channel))
        f.close()
        print(channel)

        embed = discord.Embed(title="**Changement du salon goulag**", description="C'est ici le goulag maintenant",
                              color=0xfa8072)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(
            url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQZtSN-9fn7Cig3DK"
                "-v1naUBVC_dZ4PfkOHZ7SlLkJZ3mvoSektLiHTHdw8Ug1JVnCJaQ&usqp=CAU")
        embed.add_field(name="Ceux qui ont fait de la merde finisse ici", value="les connards terminent ici",
                        inline=True)
        await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def set_goulag(ctx):
    channel = ctx.channel.id
    file_name = "goulag.txt"
    if os.stat(file_name).st_size == 0:
        f = open(file_name, 'w')
        f.write(str(channel))
        f.close()

        embed = discord.Embed(title="**Changement du salon goulag**", description="C'est ici le goulag maintenant",
                              color=0xfa8072)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(
            url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQZtSN-9fn7Cig3DK-v1naUBVC_dZ4PfkOHZ7SlLkJZ3mvoSektLiHTHdw8Ug1JVnCJaQ&usqp=CAU")
        embed.add_field(name="Ceux qui ont fait de la merde finisse ici", value="les connards terminent ici",
                        inline=True)
        await ctx.send(embed=embed)
    else:
        f = open(file_name, 'w')
        f.write(str(channel))
        f.close()
        print(channel)

        embed = discord.Embed(title="**Changement du salon goulag**", description="C'est ici le goulag maintenant",
                              color=0xfa8072)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(
            url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQZtSN-9fn7Cig3DK"
                "-v1naUBVC_dZ4PfkOHZ7SlLkJZ3mvoSektLiHTHdw8Ug1JVnCJaQ&usqp=CAU")
        embed.add_field(name="Ceux qui ont fait de la merde finisse ici", value="les connards terminent ici",
                        inline=True)
        await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, reason=None, ti=None):
    if reason is None:
        reason = "tu as enfrein les règles"
    else:
        reason = reason
    if ti is None:
        await member.ban(reason=reason)
    if ti is not None:
        tim = ti
        if str(ti).endswith("d"):
            res = ti[:-1]
            await member.send("Tu as été banni pendant " + res + " jours pour " + reason)
            await member.ban(reason=reason)
            await asyncio.sleep(int(res) * 86400)
            await member.unban()
            await ctx.send("L'utilisateur" + member.name + "à été bannie pendant " + str(res) + "pour " + reason)
        if str(ti).endswith("h"):
            res = ti[:-1]
            await member.send("Tu as été banni pendant " + str(res) + "heures pour " + reason)
            await member.ban(reason=reason)
            await asyncio.sleep(int(res) * 3600)
            await member.unban()


@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member, reason=None, ti=None):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name="mute")
    if reason is None:
        reason = "non respect des règles"
    if reason is not None:
        reason = reason
    if ti is None:
        await member.add_roles(role)
        await member.send("Tu as été mute pour" + reason)
    if ti is not None:
        if str(ti).endswith("d"):
            res = ti[:-1]
            await member.send("Tu as été mute pendant " + res + " jours pour " + reason)
            await member.add_roles(role)
            await asyncio.sleep(int(res) * 86400)
            await member.remove_roles(role)
    if ti is not None:
        if str(ti).endswith("h"):
            res = ti[:-1]
            await member.send("Tu as été mute pendant " + res + " heures pour " + reason)
            await member.add_roles(role)
            await asyncio.sleep(int(res) * 3600)
            await member.remove_roles(role)


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(804349334887333912)

    my_id = '<388734563599515649>'
    message = 'Salut {}, Bienvenue sur notre serveur discord' ' ici pas vraiment de règles juste soit cool et oublie ' \
              'pas de paramètrer ton compte si tu as le moinde problème Mp Jade, Théo ou Mathieu'.format(
        member.mention)
    await channel.send(message)


@bot.event
async def on_raw_reaction_add(payload):
    message = str(payload.message_id)

    membre = await bot.get_guild(payload.guild_id).fetch_member(payload.user_id)
    w = "SELECT * FROM Role WHERE `message_id` = '" + message + "'"
    cursor.execute(w)

    w_list = cursor.fetchall()

    for x in w_list:
        role_name = x[1]
        role = get(bot.get_guild(payload.guild_id).roles, name=role_name)
        if membre.id == 807659161222512670:
            pass
        else:
            await membre.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload):
    message = str(payload.message_id)

    membre = await bot.get_guild(payload.guild_id).fetch_member(payload.user_id)
    w = "SELECT * FROM Role WHERE `message_id` = '" + message + "'"
    cursor.execute(w)

    w_list = cursor.fetchall()

    for x in w_list:
        role_name = x[1]
        role = get(bot.get_guild(payload.guild_id).roles, name=role_name)
        if membre.id == 807659161222512670:
            pass
        else:
            await membre.remove_roles(role)


if __name__ == '__main__':
    print("lancement du bot")
    bot.run("")
