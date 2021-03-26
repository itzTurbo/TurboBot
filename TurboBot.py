import discord
from discord.ext import commands
import os
import keep_alive
import json

client = commands.Bot(command_prefix=commands.when_mentioned)

keep_alive.keep_alive()
TurboBot = os.environ.get("TurboBot")
client.run(TurboBot)