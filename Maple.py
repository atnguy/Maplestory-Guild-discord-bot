import os, discord, time, asyncio, names, random, re
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='~', case_insensitive = True)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
help_description = "Sends you pings reminding you to pop your legion wealth or when your totem is about to expire. \nEnter the amount of wealth coupons in [number] you have for this sesison. \n" + \
"[time] is what kind of wealth coupon you're using (30 minute ones by default). Enter the level or time amount" + "\n[length] is how long your current totem is in minutes. 120 minutes is by default"
@bot.command(name='totem',help =help_description)
async def totem(ctx,number:int = None,time:int = None,length: int = None):
    num = 0
    intervals = 1800
    loop = 4
    remainder = 0
    if(number != None):
        num = number
    if(time !=None):
        if(time == 1 or time == 10):
            intervals = 600
        if(time == 2 or time == 20):
            intervals = 1200
    if(length != None):
        loop = (length * 60)//intervals
        remainder = (length*60)%intervals
    await ctx.send(f"{ctx.author.mention}, your totem session has started. I will ping you within the next {length} minutes for reminders.")
    while(loop > 0 and loop*intervals >= length * 60):
        await asyncio.sleep(intervals)
        minutes_left = (((loop-1)*intervals)+remainder)/60
        if(minutes_left < 125 and minutes_left > 115):
            if(num > 0):
                await ctx.send(f"{ctx.author.mention} you have {minutes_left} minutes left on your totem and your legion wealth has expired")
                num -= 1
            else:
                await ctx.send(f"{ctx.author.mention} you have {minutes_left} minutes hour left on your totem")
        else:
            if(num > 0):
                await ctx.send(f"{ctx.author.mention} your legion wealth has expired")
                num -= 1
        loop -= 1
    
    if(remainder !=0):
        await asyncio.sleep(remainder)
    await ctx.send(f"{ctx.author.mention} your totem session has expired")
'''
@bot.command(name = "takuto",help="Spams 'fuck you @user' to a undetermined user until you use it ")
async def troll(ctx):
    #troll command. Messing with my friends when I wrote this.
    id = names.takuto()
    who = ctx.message.author.id
    if(who == 266035355013218304):
        #making sure guen doesn't abuse this command
        id = 266035355013218304
        await ctx.author.send(f"Stop using this command <@{id}>")
    else:
        await ctx.send(f"Fuck you <@{id}>")
'''
@bot.command(name = "ror4",help="Alice decides if you should get a ror4 or not today")
async def alicesaysno(ctx):
    num = random.randint(0,299)
    if(num<1):
        await ctx.send("Today is the day")
    else:
        await ctx.send("Not today XD. Go fry your brain more at oz.")
@bot.command(name = "hi", help = "Alice will say hi to you")
async def sayshi(ctx):
    await ctx.send(f"hi <{ctx.author.nickname}>")

@bot.listen('on_message')
async def giverole(message):
   
    if(message.channel.id == 701497757382344764):
        if(message.author.id == bot.user.id):
            #do nothing
            print("ignore bot message")
        else:
            #if in names channel
            rolelist = message.author.roles
            
            action = True
            user = message.author
            memberrole = discord.utils.get(user.guild.roles,name = "Members")
            #waiting for joe's permission to uncomment the followign block of code
            '''
            for role in rolelist:
                if (role.name == "Members"):
                    action = False
            if(action):
            await user.add_roles(memberrole)
            '''
            informat = re.search("^\w+ \[{1}\w+\]{1}$",message.content)
            if informat and len(rolelist) == 1:
                #assuring that you're roleless and you need a name
                await user.edit(nick=message.content)
            elif re.search("^\w+\[{1}\w+\]{1}$",message.content) and len(rolelist) == 1:
                await user.edit(nick=message.content)
            else:
                if(len(rolelist)>1):
                    #only offices should have access to the #names channel
                    print("Ignoring officer message")
                else:
                    await message.channel.send("I'm sorry thats not the correct format. Please type as ign [name] or ign[name].")
        
    '''
    if(message.channel.id == 693706900767899648):
        informat = re.search("^\w+\[{1}\w+\]{1}$",message.content)
        if informat:
            print("success")
        else:
            print("failure")
    #test code for the regex
    '''
bot.run(TOKEN)