import asyncio
import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="c!")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Connected and ready to use!")
    game = discord.Game("Creamcake c!help")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def ping(ctx):
    embed = discord.Embed(colour=ctx.author.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Roundtrip took {round(bot.latency * 1000)} ms")
    embed.set_footer(text=f"Requested by {ctx.author}")
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def coinflip(ctx):
    flip = ("Tails", "Heads")
    coin = random.choice(flip)
    await ctx.send(coin)

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Title',
        description='This is a test',
        colour=ctx.author.color
    )
    embed.set_footer(text='Footer test')
    embed.set_thumbnail(url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.taste.com.au%2FmqX5ncxF%2Fw1200-h630-cfill%2Ftaste%2F2016%2F11%2Fzabaglione-ice-cream-cake-99052-1.jpeg&imgrefurl=https%3A%2F%2Fwww.taste.com.au%2Frecipes%2Fzabaglione-ice-cream-cake%2F846f7a37-1afd-4526-9dfb-054150c35131&docid=LOh1fq9BQgW10M&tbnid=_EqCC9IEJHiJPM%3A&vet=10ahUKEwjkjIfQrdfjAhXBdHAKHdM5B2kQMwhHKAUwBQ..i&w=1200&h=630&bih=657&biw=1366&q=creamcake&ved=0ahUKEwjkjIfQrdfjAhXBdHAKHdM5B2kQMwhHKAUwBQ&iact=mrc&uact=8')
    embed.set_author(name='Author test', icon_url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.taste.com.au%2FmqX5ncxF%2Fw1200-h630-cfill%2Ftaste%2F2016%2F11%2Fzabaglione-ice-cream-cake-99052-1.jpeg&imgrefurl=https%3A%2F%2Fwww.taste.com.au%2Frecipes%2Fzabaglione-ice-cream-cake%2F846f7a37-1afd-4526-9dfb-054150c35131&docid=LOh1fq9BQgW10M&tbnid=_EqCC9IEJHiJPM%3A&vet=10ahUKEwjkjIfQrdfjAhXBdHAKHdM5B2kQMwhHKAUwBQ..i&w=1200&h=630&bih=657&biw=1366&q=creamcake&ved=0ahUKEwjkjIfQrdfjAhXBdHAKHdM5B2kQMwhHKAUwBQ&iact=mrc&uact=8')
    embed.add_field(name='Field test', value='Field Value Test', inline=False)
    embed.add_field(name='Field test', value='Field Value Test', inline=True)
    embed.add_field(name='Field test', value='Field Value Test', inline=True)

    await ctx.send(embed=embed)

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    response = ['It is certain',
                'Ask again later',
                'Yes',
                'No',
                'Of course',
                'Of course',
                'Of course not',
                'Without a doubt',
                'Probably, Probably not']
    embed = discord.Embed(
        title=f'{question}',
        description=f'{random.choice(response)}',
        colour=ctx.author.color
    )
    await ctx.send(embed=embed)
response2 = ['Relevant',
             'Irrelevant',
             'Useless',
             'Cool',
             'Very Brutal',
             'Dumb',
             'Helpful',]

@bot.command()
async def rate(ctx, *, ration):
    await ctx.channel.send(f"{ctx.author} I rate {ration} {random.randint(0, 100)}% {random.choice(response2)}")



bot.run(str(os.environ.get("NjAwMjYyNzUyNDEzNjc5NjI2.XSxMaA._AaS70LRwuayIAdMk4WoOVn9jf8")))
