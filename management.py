import asyncio
import discord
import openpyxl

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("온라인이에요!")

@client.event
async def on_message(message):
    if message.content  ==  '관리원 도움':
        embed = discord.Embed(title="관리원 명령어 도움말", color=0xff00)
        embed.add_field(name="관리원 명령어 아파트", value="아파트 관련 명령어입니다.", inline=True)
        embed.add_field(name="관리원 명령어 백화점", value="백화점 관련 명령어입니다.", inline=True)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '관리원 명령어 아파트':
        embed = discord.Embed(title="관리원 아파트 명령어 도움말", color=0xff00)
        embed.add_field(name="관리원 호출", value="관리원을 호출하는 기능입니다. (따로 기능은 없습니다.)")
        embed.add_field(name="경비원 호출", value="경비원을 호출하는 기능입니다.")
        embed.add_field(name="관리원 헌법", value="즐거운 아파트의 법에 대한 정보입니다.")
        embed.add_field(name="관리원 아파트정보", value="즐거운 아파트에 대한 정보입니다.")
        embed.add_field(name="관리원 침입자경보", value="침입자 경고 시스템입니다.")
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content  == '관리원 호출':
        await message.channel.send("무엇을 도와드릴까요?")

    if message.content == '경비원 호출':
        await message.channel.send("<#668612325921783818> 이나 <#667311201776173057> 에서 문의해주세요.")    

    if message.content == '관리원 헌법':
        await message.channel.send("즐거운 아파트에 법은 <#665367497628712970> 에서 확인하실 수 있습니다.")
    
    if message.content == '관리원 아파트정보':
        embed = discord.Embed(title="즐거운 아파트 정보", color=0xff00)
        embed.add_field(name="즐거운 아파트", value=f"즐거운 아파트는 A동과 B동으로 구성되어 있으며, 101호부터 410호까지 총 80세대가 입주할 수 있으며\n 현재 {len(client.users)} 세대가 입주해 있습니다.")
        embed.set_footer(text="{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '관리원 침입자경보':
        await message.channel.send("경비원을 호출하는 중...")
        await message.channel.send("누구인가? 누가 무단침입을 했는가?")

    if message.content == '관리원 명령어 백화점':
        embed = discord.Embed(title="관리원 백화점 명령어 도움말", color=0xff00)
        embed.add_field(name="관리원 백화점정보", value="현재 백화점에 입점해있는 상가들 명단을 볼 수 있습니다.", inline=True)
        embed.add_field(name="관리원 상점정보 <상점이름>", value="백화점에 입점해있는 상가의 정보를 볼 수 있습니다.", inline=True)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    
    if message.content  == '관리원 백화점정보':
        embed = discord.Embed(title="즐거운 아파트 백화점 입점 정보", color=0xff00)
        embed.add_field(name="마인문고", value="이슷님의 `14F`", inline=True)
        embed.add_field(name="H.A.dessert", value="주신아님의 `H.A.dessert`", inline=True)
        embed.add_field(name="스카이팀 전자아울렛", value="스카이팀님의 `스카이팀 전자아울렛`", inline=True)
        embed.add_field(name="썸띵데이베이커리", value="SomethingDay님의 `썸띵베이커리`", inline=True)
        embed.add_field(name="룰루랄라 키즈카페", value="SUUT님의 `룰루랄라 키즈카페`", inline=True)
        embed.add_field(name="아디닭스", value="HEALING님의 `아디닭스`", inline=True)
        embed.add_field(name="봇 가게", value="키키님의 `봇 가게`", inline=True)
        embed.add_field(name="지나이키", value="♥G999♥님의 `지나이키`", inline=True)
        embed.add_field(name="ART HOUSE", value="SYEONG님의 `ART HOUSE`", inline=True)
        embed.add_field(name="GUCHICKEN", value="RIDEE님의 `GUCHICKEN`", inline=True)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    
    if message.content  == '관리원 상점정보':
        await message.channel.send("```올바른 사용법: 관리원 상점정보 <상점이름>```")

    if message.content  == '관리원 상점정보 14F':
        embed = discord.Embed(title="백화점 상점 정보", color=0xff00)
        embed.add_field(name="14F 정보", value="14F는 입점 준비중입니다.", inline=True)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content  == '관리원 상점정보 H.A.dessert':
        embed = discord.Embed(title="백화점 상점 정보", color=0xff00)
        embed.add_field(name="H.A.dessert 정보", value="H.A.dessert 는 Happy Apart dessert의 약자이고 말 그대로 디저트카페입니다.\n파는 것은 음료류와 디저트류 등을 팝니다.", inline=True)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content  == '관리원 상점정보 스카이팀 전자아울렛':
        embed = discord.Embed(title="백화점 상점 정보", color=0xff00)
        embed.add_field(name="스카이팀 전자아울렛 정보", value="스카이팀 전자아울렛에서는 전자기기를 판매하고 있습니다.", inline=True)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '관리원 상점정보 썸띵베이베이커리':
        embed = discord.Embed(title="백화점 상점 정보", color=0xff00)
        embed.add_field(name="썸띵베이베이커리 정보", value="빵 만들건데오", inline=True)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '관리원 상점정보 룰루랄라 키즈카페':
        embed = discord.Embed(title="백화점 상점정보", color=0xff00)
        embed.add_field(name="룰루랄라 키즈카페 정보", value=":loudspeaker: 백화점 상가 입점!!!!!!\n :mega: 룰루랄라 키즈카페!~\n :white_check_mark: 저희 룰루랄라 키즈카페는 유치원생까지만 받아 초등학생이 독차지 (?) 하는 일은 없을 것 입니다.\n :white_check_mark: 놀이터, 방방, 모래 놀이실, 오락실, 장난감 뽑기로 이루어져 있어 4세부터 7세까지의 연령대 중 모든 어린이들이 놀수있도록 설계했습니다.\n :white_check_mark: 청결하고 아이들이 놀수있는 안전한 최적의 공간!! 많이들 놀러와주세요!!!!!!\n :speech_left: 부모님들이 쉴수 있는 카페도 있어요~~~", inline=True)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '관리원 상점정보 아디닭스':
        embed = discord.Embed(title="백화점 상점 정보", color=0xff00)
        embed.add_field(name="아디닭스 정보", value=":one: 아디닭스 후라이드 치킨 11000원\n :two: 아따 맛이좋다오 양념 치킨 12000원\n :three: 아딥게 맵네 고추치킨\n :four: 이것좀 먹게 닭쳐유 간장치킨\n :thumbsup: 쿠폰 10개 모을 시 양념 감자튀김 무료\n :thumbsup: 단골손님 올 때마다 콜라 무료 지급", inline=True)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '관리원 상점정보 봇 가게':
        embed = discord.Embed(title="백화점 상점 정보", color=0xff00)
        embed.add_field(name="봇 가게 정보", value="업데이트 예정입니다.")
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '관리원 상점정보 지나이키':
        embed = discord.Embed(title="백화점 상점 정보", color=0xff00)
        embed.add_field(name="지나이키 정보", value="업데이트 예정입니다.")
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '관리원 상점정보 ART HOUSE':
        embed = discord.Embed(title="백화점 상점 정보", color=0xff00)
        embed.add_field(name="ART HOUSE 정보", value="업데이트 예정입니다.")
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '관리원 상점정보 GUCHICKEN':
        embed = discord.Embed(title="백화점 상점 정보", color=0xff00)
        embed.add_field(name="GUCHICKEN 정보", value="업데이트 예정입니다.")
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    
async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        game = discord.Game("시범 운영중인 서비스입니다.")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game(f'{len(client.users)}명의 입주자분들이 즐거운 아파트에 거주하고 있어요!')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game("관리원 도움을 입력해보세요!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
client.loop.create_task(my_background_task())

client.run(str(os.environ.get('BOT_TOKEN')))
