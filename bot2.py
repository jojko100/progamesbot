import discord
import json
import os
from discord.ext import commands


TOKEN = 'NzIxMzAyMTk4NzY3NTgzMzM0.Xu9Iag.tzgdyd40Bgdf4F1JkS4m91rtcZE'

client = commands.Bot(command_prefix='.')
client.remove_command('help')
    

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Coding my code'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    
@client.event
async def on_message(message):
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Stastne a vesele!')      
        
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
            
                     
               
def admin(ctx):
    return ctx.author.id == 681536823964860466    
    return ctx.author.id == 690437070841446400
    return ctx.author.id == 326044727361142785           

#@client.command()
#async def add(ctx, left : int, right : int):
#    await ctx.send(left + right)

@client.command()
@commands.check(admin)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def pomoc(ctx):
    await ctx.send('1 /n 2 /n 3 /n 4 /n 5')       


        
        
client.run(TOKEN)