from tokens import TOKEN
import discord
from discord.ext import commands
import random, logging
import asyncio
import requests
from get_weather import get_weather, get_weather_days
from truth_dare import truth, dare, append_truth, append_dare, get_quote
from translater import translate

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True


class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.city = 'saratov'

    @commands.command(name='random_user')
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

    @commands.command(name='truth')
    async def truth(self, ctx, member):
        await ctx.send(f'{member} {truth()}')

    @commands.command(name='dare')
    async def dare(self, ctx, member):
        await ctx.send(f'{member} {dare()}')

    @commands.command(name='append_truth')
    async def append_t(self, ctx, *question):
        append_truth(question)
        await ctx.send('done!')

    @commands.command(name='append_dare')
    async def append_d(self, ctx, *action):
        append_dare(action)
        await ctx.send('done!')

    @commands.command(name='translate')
    async def translate(self, ctx, *words):
        await ctx.send(translate(words[:-1], words[-1]))

    @commands.command(name='quote')
    async def quote(self, ctx):
        text = get_quote().split('-')[0]
        author = get_quote().split('-')[1]
        await ctx.send(f"_{text}_ - {author}")

    @commands.command(name='info')
    async def help(self, ctx):
        embed_obj = discord.Embed()
        embed_obj.description = "текст"
        await ctx.send(f"```set_timer - таймер, время указывается в секундах\n"
                       f"cat/dog - рандомные картинки с милыми животными\n"
                       f"create_pack - создание пака для викторины\n"
                       f"place - смена местаположения для отображения погоды\n"
                       f"current - прогноз погоды на сегодня в указанном местоположении\n"
                       f"weather - прогноз погоды на несколько дней (до 8) в указанном местоположении\n"
                       f"random_user - рандомный пользователь в канале\n"
                       f"truth - задание для правды в правда или действие\n"
                       f"dare - задание для действия в правда или действие\n"
                       f"translate - перевод введенного текста, вводится сначала текст для перевода, "
                       f"потом язык, на который нужно перевести\n"
                       f"append_dare/append_truth - добавление заданий для правды или действия\n"
                       f"get_quote - цитаты известных```")


bot = commands.Bot(command_prefix='!', intents=intents)
bot.add_cog(Commands(bot))
bot.run(TOKEN)
