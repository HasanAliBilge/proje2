import discord
from discord.ext import commands
from config import Token, DATABASE
from logic import DB_Manager, Quiz

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
quiz = Quiz(DB_Manager(DATABASE))
user_scores = {}
current_questions = {}

@bot.event
async def on_ready():
    print(f'{bot.user.name} çalışıyor!')

@bot.command()
async def soru(ctx):
    user_id = ctx.author.id
    if data := quiz.get_question():
        country, capital, continent_id = data
        current_questions[user_id] = (country, capital, continent_id)
        await ctx.send(f"{country} başkenti nedir? ({quiz.get_points(continent_id)} puan)")

@bot.command()
async def cevap(ctx, *, answer):
    user_id = ctx.author.id
    
    if user_id not in current_questions:
        return await ctx.send("Önce !soru komutuyla soru almalısınız!")

    country, capital, continent_id = current_questions.pop(user_id)
    user_scores.setdefault(user_id, 0)
    
    if quiz.check_answer(answer, capital):
        puan = quiz.get_points(continent_id)
        user_scores[user_id] += puan
        await ctx.send(f"✅ Doğru! +{puan} puan. Toplam: {user_scores[user_id]}")
    else:
        await ctx.send(f"❌ Yanlış! Doğru cevap: {capital}")

@bot.command()
async def puan(ctx):
    await ctx.send(f"Puanınız: {user_scores.get(ctx.author.id, 0)}")

bot.run(Token)