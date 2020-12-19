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
        game = discord.Game("Powerd by PYTHON")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("24시간 풀 가동중...")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("공식주소: discord.gg/nEzPCjd")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("서버문의: 우정#9444 ")
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
        await channel.send('업데이트 확률 1%')
    if message.content.startswith('알겠음'):
        channel = message.channel
        await channel.send('알겠지?')
    if message.content.startswith('ㄱㄷ'):
        channel = message.channel
        await channel.send('못기다리겠는데?')
    if message.content.startswith('미안'):
        channel = message.channel
        await channel.send('ㅇㅅㅇ?')
    if message.content.startswith('부스트'):
        channel = message.channel
        await channel.send('6000원의 행복')
    if message.content.startswith('니트로'):
        channel = message.channel
        await channel.send('15000원의 행복')
    if message.content.startswith('싫어'):
        channel = message.channel
        await channel.send('아잉')
    if message.content.startswith('헐'):
        channel = message.channel
        await channel.send('헐')
    if message.content.startswith('바보'):
        channel = message.channel
        await channel.send('너도 ㅋ')
    if message.content.startswith('멍청이'):
        channel = message.channel
        await channel.send('안들려~')
    if message.content.startswith('마'):
        channel = message.channel
        await channel.send('동석')
    if message.content.startswith('하'):
        channel = message.channel
        await channel.send('하')
    if message.content.startswith('음'):
        channel = message.channel
        await channel.send('뭘 고민해 ㅋ')
    if message.content.startswith('신기'):
        channel = message.channel
        await channel.send('나도 내가 신기해 ㅋㅋ')
    if message.content.startswith('오호'):
        channel = message.channel
        await channel.send('5HO')
    if message.content.startswith('님'):
        channel = message.channel
        await channel.send('왜부름?')
    if message.content.startswith(';;'):
        channel = message.channel
        await channel.send('땀 닦아줄게')
    if message.content.startswith('ㅠㅠ'):
        channel = message.channel
        await channel.send('울지마')
    if message.content.startswith('ㅋㅋㄹㅃㅃ'):
        channel = message.channel
        await channel.send('ㅋㅋㄹㅃㅃ')
    if message.content.startswith('임포스터'):
        channel = message.channel
        await channel.send('Kill')
    if message.content.startswith('크루원'):
        channel = message.channel
        await channel.send('Report')
    if message.content.startswith('어몽어스'):
        channel = message.channel
        await channel.send('ඞ')
    if message.content.startswith('5초 카운트'):
        channel = message.channel
        await channel.send('***※경고: 해당 명령어를 연속으로 사용하지 마십시오.***')
        await channel.send('***※경고: 해당 기능은 PC버전에서의 사용을 권장합니다.***')
        await channel.send('5초 카운트를 **시작**합니다...')
        await channel.send('> 5')
        await channel.send('> 4')
        await channel.send('> 3')
        await channel.send('> 2')
        await channel.send('> 1')
        await channel.send('5초 카운트를 **종료**합니다...')
    if message.content.startswith('파이썬'):
        channel = message.channel
        await channel.send('나도 파이썬으로 만들어짐')
    if message.content.startswith('보자보자'):
        channel = message.channel
        await channel.send('어디보자')
        await channel.send('너 두고 보자')
    if message.content.startswith('이름이 뭐야'):
        channel = message.channel
        await channel.send('Hi my name iS 압둘알리과로사')
        await channel.send('지금부터 내가 너희들에게 폭탄같은 랩을 전사')
    if message.content.startswith('나 어때?'):
        channel = message.channel
        await channel.send('잘생겼어:)')
        await channel.send('사실은...')
        await channel.send('거짓말이야, 못생겼어.')
    if message.content.startswith('저기요'):
        channel = message.channel
        await channel.send('안되요!')
        await channel.send('싫어요!')
        await channel.send('하지마세요!')
    if message.content.startswith('죄송합니다'):
        channel = message.channel
        await channel.send('괜찮아요, 다음부터 조심합시다!')
    if message.content.startswith('휴'):
        channel = message.channel
        await channel.send('한숨 쉬지마, 땅 꺼지겠다 ㅋㅋ;;')
    if message.content.startswith('노래불러줘'):
        channel = message.channel
        await channel.send('떴다~ 떴다~ 비행기~ 🎶')
        await channel.send('날아라~ 날아라~ 🎶')
        await channel.send('높이~ 높이~ 날아라~ 우리 비행기~ 🎶')
        
access_token = os.environ['BOT_TOKEN']        
client.run(access_token)
