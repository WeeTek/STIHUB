import discord
from discord.ext import commands
from discord.utils import get
import os
import re
import time

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)


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
    id = role.name
    msg_id = message.id
    file_role = "role.txt"
    f = open(file_role, 'a')
    f.write(str(role.name) + "," + str(msg_id) + "\n")
    f.close()
    await message.add_reaction("✅")


@bot.command()
@commands.has_permissions(administrator=True)
async def goulag(ctx, member: discord.Member):
    message = 'Aller hop hop hop au goulag {}'.format(
        member.mention)
    await ctx.send(message)
    await ctx.send("https://risibank.fr/cache/stickers/d534/53401-full.gif")


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
async def ban(ctx, member: discord.Member = None, reason=None, time=None):
    if time == None:

        if member == None or member == ctx.message.author:
            await ctx.channel.send("Tu peux pas te ban toi même")
            return
        if reason is None:
            reason = "tu es moche!"
        message = f"Tu à été ban de {ctx.guild.name} car {reason}"
        await ctx.channel.send(f"{member} à été banni")
        await member.send(message)
        await member.ban(reason=reason)
        # await ctx.guild.ban(member, reason=reason)
        await ctx.send("https://media.tenor.com/images/7ca9d4fd492df7b05852f033c84727aa/tenor.gif")
    if time is not None:
        t = time
        today = time.time()
        ratio = 0
        id = None
        m = None
        if "d" in t:
            ratio = 86400
            m = "jour"
        if "h" in t:
            ratio = 3600
            m = "heurs"
        if "y" in t:
            ratio = 31536000
            m = "année"
        if "m" in t:
            ratio = 2592000
            m = "mois"
        if "w" in t:
            ratio = 604800
            m = "semaine"
        if member == None or member == ctx.message.author:
            await ctx.channel.send("Tu peux pas te ban toi même")
            return
        if reason is None:
            reason = "tu es moche!"
        message = f"Tu à été ban de {ctx.guild.name} car {reason} pour " + t[:-1] + m
        await member.send(message)
        await member.ban(reason=reason)
        file_name = "ban.txt"
        f = open(file_name, "w")
        f.write(today)


@bot.event
async def on_member_join(member):
    file_name = "welcome.txt"
    f = open(file_name, 'r')
    info = f.readlines()
    print(info[0])
    f.close()
    channel = bot.get_channel(int(info[0]))

    my_id = '<388734563599515649>'
    message = 'Salut {}, Bienvenue sur notre serveur discord' ' ici pas vraiment de règles juste soit cool et oublie ' \
              'pas de paramètrer ton compte si tu as le moinde problème Mp Jade, Théo ou Mathieu'.format(
        member.mention)
    await channel.send(message)


@bot.event
async def on_raw_reaction_add(payload):
    message = str(payload.message_id)
    file1 = open("role.txt", "r")

    membre = await bot.get_guild(payload.guild_id).fetch_member(payload.user_id)
    flag = 0
    index = 0

    for line in file1:
        index += 1

        if message in line:
            flag = 1
            most_divided_line = line
            divided = most_divided_line.split(",")
            role_to_give = get(bot.get_guild(payload.guild_id).roles, name=divided[0])
            await membre.add_roles(role_to_give)

            break

    if flag == 0:
        print('String', message, 'Not Found')
    else:
        print('String', message, 'Found In Line', index)

    file1.close()


@bot.event
async def on_raw_reaction_remove(payload):
    message = str(payload.message_id)
    file1 = open("role.txt", "r")

    membre = await bot.get_guild(payload.guild_id).fetch_member(payload.user_id)
    flag = 0
    index = 0

    for line in file1:
        index += 1

        if message in line:
            flag = 1
            most_divided_line = line
            divided = most_divided_line.split(",")
            role_to_give = get(bot.get_guild(payload.guild_id).roles, name=divided[0])
            await membre.remove_roles(role_to_give)

            break

    if flag == 0:
        pass
    else:
        print('String', message, 'Found In Line', index)

    file1.close()


if __name__ == '__main__':
    print("lancement du bot")
    bot.run("ODA3NjU5MTYxMjIyNTEyNjcw.YB7NNQ.ZRjzCoNQxw5A5vTb13-vPs9JMCE")
