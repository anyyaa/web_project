from tokens import TOKEN
import discord
from discord.ext import commands
import random, logging
import asyncio
import requests
import json
from get_weather import get_weather, get_weather_days

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


class RandomThings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.city = 'saratov'

    @commands.command(name='roll_dice')
    async def roll_dice(self, ctx, count):
        res = [random.choice(dashes) for _ in range(int(count))]
        await ctx.send(" ".join(res))

    @commands.command(name='randint')
    async def my_randint(self, ctx, min_int, max_int):
        num = random.randint(int(min_int), int(max_int))
        await ctx.send(num)

    @commands.command(name='set_timer')
    async def timer(self, ctx, seconds):
        resp = f"the timer starts in {seconds} seconds"
        await ctx.send(resp)
        await asyncio.sleep(seconds)
        await ctx.send('the time x has come')

    @commands.command(name='cat')
    async def cat(self, ctx):
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        json_response = response.json()
        resp = json_response[0]["url"]
        await ctx.send(resp)

    @commands.command(name='dog')
    async def dog(self, ctx):
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        print(response)
        json_response = response.json()
        print(json_response)
        resp = json_response["message"]
        await ctx.send(resp)

    @commands.command(name='create_pack')
    async def create_pack(self, ctx):
        await ctx.send(f'Для создания пака перейдите по ссылке: ')

    @commands.command(name='place')
    async def change_place(self, city='Moscow'):
        self.city = city

    @commands.command(name='current')
    async def weather_rn(self, ctx):
        await ctx.send(get_weather(self.city))

    @commands.command(name='weather')
    async def weather_with_days(self, ctx, days):
        a = get_weather_days(days, self.city)
        print(a)
        for i in range(int(days)):
            await ctx.send(f'{a[0][i]}, {a[1][i]}, {a[2][i]}, {a[3][i]}, {a[4][i]}')


bot = commands.Bot(command_prefix='!', intents=intents)
bot.add_cog(RandomThings(bot))
bot.run(TOKEN)
