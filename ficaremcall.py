import discord
import asyncio

token = "MTI0Mzk4NDUxMjA3NDEyMTMyMA.Gq1oDO.Ay9zQkaPeNqMGqFtXVDJAN1uUmi21zqhLE49DA"  # Seu token de usuário
voice_channel_id = 1373020817679712329  # ID do canal de voz

client = discord.Client(self_bot=True)

@client.event
async def on_ready():
    print(f"✅ Logado como {client.user}")

    channel = client.get_channel(voice_channel_id)

    if channel and isinstance(channel, discord.VoiceChannel):
        try:
            await channel.connect()
            print("🎧 Conectado ao canal de voz.")
        except Exception as e:
            print(f"❌ Erro ao conectar: {e}")
    else:
        print("❌ Canal de voz inválido.")

client.run(token)
