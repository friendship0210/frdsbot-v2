import asyncio
import discord
import os

client = discord.Client()

# 복사해 둔 토큰을 your_token에 넣어줍니당
token = "Nzc3MzQyMjI3OTU2NzYwNTg4.X7CCXQ.YWr2-iHC918itckciJ4pWsff4iA"

# 봇이 구동되었을 때 동작되는 코드
@client.event
async def on_ready():
    print("로그인 된 봇:") #화면에 봇의 아이디, 닉네임이 출력되는 코드
    print(client.user.name)
    print(client.user.id)
    print("===========")
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("시작하는 중...")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("Made by 우정#9444")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("24시간 풀 가동중...")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
        


# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('안녕하세요'):
        channel = message.channel
        await channel.send('Hello!')
    if message.content.startswith('ㅎㅇ'):
        channel = message.channel
        await channel.send('Hi')
    if message.content.startswith('우정'):
        channel = message.channel
        await channel.send('Friendship')
    if message.content.startswith('공식주소'):
        channel = message.channel
        await channel.send('discord.gg/nEzPCjd')
    if message.content.startswith('머리부터'):
        channel = message.channel
        await channel.send('발끝까지')
    if message.content.startswith('어이'):
        channel = message.channel
        await channel.send('뭐')
    if message.content.startswith('야'):
        channel = message.channel
        await channel.send('왜')
    if message.content.startswith('우정아'):
        channel = message.channel
        await channel.send('왜불러')
    if message.content.startswith('뭐해'):
        channel = message.channel
        await channel.send('놀아')
    if message.content.startswith('ㅋㅋㅋ'):
        channel = message.channel
        await channel.send('ㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
    if message.content.startswith('봇상태'):
        channel = message.channel
        await channel.send('24시간 풀 가동!')
    if message.content.startswith('주인이 누구야?'):
        channel = message.channel
        await channel.send('우정')
    if message.content.startswith('ㅇㅋ'):
        channel = message.channel
        await channel.send('ㅇㅇ')
    if message.content.startswith('배고파'):
        channel = message.channel
        await channel.send('밥먹어 그럼')
    if message.content.startswith('디스코드'):
        channel = message.channel
        await channel.send('2015년 5월 출시된 채팅 메신저 프로그램!')
    if message.content.startswith('?'):
        channel = message.channel
        await channel.send('??')
    if message.content.startswith('처벌해'):
        channel = message.channel
        await channel.send('응 안해 ㅋ')
    if message.content.startswith('잘가'):
        channel = message.channel
        await channel.send('잘가고~')
    if message.content.startswith('졸려'):
        channel = message.channel
        await channel.send('자장가 불러줄까?')
    if message.content.startswith('Friendship hub'):
        channel = message.channel
        await channel.send('FR13NDSH1P HU3')
    if message.content.startswith('응'):
        channel = message.channel
        await channel.send('아니야')
    if message.content.startswith('반갑습니다'):
        channel = message.channel
        await channel.send('Welcome!')
    if message.content.startswith('인성'):
        channel = message.channel
        await channel.send('문제있어')
    if message.content.startswith('개인주의'):
        channel = message.channel
        await channel.send('너 개인주의야?')
    if message.content.startswith('이만'):
        channel = message.channel
        await channel.send('ㅃㅃ')
    if message.content.startswith('ㅇㅇ'):
        channel = message.channel
        await channel.send('ㅇㅇ는 반말이고 ㅋ')
    if message.content.startswith('감사합니다'):
        channel = message.channel
        await channel.send('유어 웰 컴!')
    if message.content.startswith('네'):
        channel = message.channel
        await channel.send('ok')
    if message.content.startswith('아니'):
        channel = message.channel
        await channel.send('뭐가 아니야 ㅋㅋㅋ')
    if message.content.startswith('업데이트'):
        channel = message.channel
        await channel.send('업데이트 확률 0.001%')
    if message.content.startswith('알겠음'):
        channel = message.channel
        await channel.send('알겠지?')
    if message.content.startswith('ㄱㄷ'):
        channel = message.channel
        await channel.send('10초 셀게')
    if message.content.startswith('미안'):
        channel = message.channel
        await channel.send('ㅇㅅㅇ?')
        
        
access_token = os.environ['BOT_TOKEN']        
client.run(access_token)
