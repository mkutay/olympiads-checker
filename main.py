import csolver
import scraper
import dotenv
import os
import discord
import asyncio

dotenv.load_dotenv()
sessionId = os.getenv("DWRSESSIONID")
tc = os.getenv("TC")
url = "https://ebideb.tubitak.gov.tr/olimpiyatSinavSonucSistemi.htm"

def bot():
  ret = scraper.scrape(sessionId, tc, url, "gh.jpg") # you could actually use anything for your session id

  if ret == 0:
    ret = bot()
  
  return ret

def check():
  if bot() == 1:
    return "results are out (for informatics birinci asama)"
  else:
    return "results are not out (for informatics birinci asama)"

client = discord.Client(intents=discord.Intents.all())
token = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  asyncio.ensure_future(send_message())

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if "birinci asama" not in msg:
    return
  
  response = check()

  await message.channel.send(response)

async def send_message():
  await client.wait_until_ready()
  channel = client.get_channel(1012032367382233100)
  counter = 1

  while not client.is_closed():
    message = check()
    await channel.send(message)
    counter += 1
    await asyncio.sleep(2)

loop = asyncio.get_event_loop()
try:
  loop.run_until_complete(client.login(token))
  loop.run_until_complete(client.connect())
except KeyboardInterrupt:
  loop.run_until_complete(client.close())
finally:
  loop.close()