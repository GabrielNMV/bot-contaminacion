import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')



@bot.command('comandos')
async def comandos(ctx):
    await ctx.send("Los comandos son $contaminacion, $como_evitar, $imagenes")

@bot.command('imagenes')
async def imagenes(ctx):
    imagesLista = random.choice(os.listdir('m1l_pypro/actividades_2/images2'))
    with open(f"m1l_pypro/actividades_2/images2/{imagesLista}", 'rb') as f:
        picture = discord.File(f)   
    await ctx.send(file=picture)

@bot.command('como_evitar')
async def como_evitar(ctx):
    await ctx.send("No tirar basura al suelo, apagar las luces de tu casa cuando no las necesites, no usar tanta agua cuando sea inecesario")

@bot.command('contaminacion')
async def contaminacion(ctx):
    await ctx.send("La contaminación ambiental es uno de los principales problemas que se está dando a nivel global desde ya hace mucho tiempo, afectando a todo el planeta, a su biodiversidad y a la salud de las personas. Son diferentes los tipos de contaminación que existen, todo depende de la zona o elemento que se ve afectado y del tipo de agentes contaminantes que producen el problema. Toda contaminación está causando grandes consecuencias a las que hay que poner solución. Aún estamos a tiempo de paliar los efectos de la contaminación ambiental.")




bot.run)
