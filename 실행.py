import os
import discord
import time
import asyncio
import requests
import openpyxl
import json
import re
import random

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("섹스")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="문재인")
    await member.add_roles(role)
    channel = 708182848645103706
    await member.send(f'{member.mention}님 환영합니다!')
    await client.get_channel(int(channel)).send(f"{member.mention}님 어서오세요!")


@client.event
async def on_member_remove(member):
    channel = 708182888851701871
    await client.get_channel(int(channel)).send(f"{member.mention}님이 퇴장하셨습니다.")


@client.event
async def on_message(message):
    if message.content.startswith("!아이디"):
        await message.author.send(message.author.id)
    if message.content.startswith("!삭제"):
        role1 = discord.utils.get(message.author.guild.roles, name="빨간색") #빨
        role2 = discord.utils.get(message.author.guild.roles, name="주황색") #주
        role3 = discord.utils.get(message.author.guild.roles, name="노란색") #노
        role4 = discord.utils.get(message.author.guild.roles, name="초록색") #초
        role5 = discord.utils.get(message.author.guild.roles, name="파란색") #파
        role6 = discord.utils.get(message.author.guild.roles, name="남색") #남
        role7 = discord.utils.get(message.author.guild.roles, name="보라색") #보
        await message.author.remove_roles(role1)
        await message.author.remove_roles(role2)
        await message.author.remove_roles(role3)
        await message.author.remove_roles(role4)
        await message.author.remove_roles(role5)
        await message.author.remove_roles(role6)
        await message.author.remove_roles(role7)
        await message.channel.send(f"{message.author.mention} 변경 완료!")
        await message.author.send(f'{message.author.mention} 변경 완료!')
    if message.content.startswith("!빨"):
        role1 = discord.utils.get(message.author.guild.roles, name="빨간색") #빨
        role2 = discord.utils.get(message.author.guild.roles, name="주황색") #주
        role3 = discord.utils.get(message.author.guild.roles, name="노란색") #노
        role4 = discord.utils.get(message.author.guild.roles, name="초록색") #초
        role5 = discord.utils.get(message.author.guild.roles, name="파란색") #파
        role6 = discord.utils.get(message.author.guild.roles, name="남색") #남
        role7 = discord.utils.get(message.author.guild.roles, name="보라색") #보
        await message.author.remove_roles(role2)
        await message.author.remove_roles(role3)
        await message.author.remove_roles(role4)
        await message.author.remove_roles(role5)
        await message.author.remove_roles(role6)
        await message.author.remove_roles(role7)
        time.sleep(1)
        await message.author.add_roles(role1)
        await message.channel.send(f"{message.author.mention} 변경 완료!")
        await message.author.send(f'{message.author.mention} 변경 완료!')
    if message.content.startswith("!주"):
        role1 = discord.utils.get(message.author.guild.roles, name="빨간색") #빨
        role2 = discord.utils.get(message.author.guild.roles, name="주황색") #주
        role3 = discord.utils.get(message.author.guild.roles, name="노란색") #노
        role4 = discord.utils.get(message.author.guild.roles, name="초록색") #초
        role5 = discord.utils.get(message.author.guild.roles, name="파란색") #파
        role6 = discord.utils.get(message.author.guild.roles, name="남색") #남
        role7 = discord.utils.get(message.author.guild.roles, name="보라색") #보
        await message.author.remove_roles(role1)
        await message.author.remove_roles(role3)
        await message.author.remove_roles(role4)
        await message.author.remove_roles(role5)
        await message.author.remove_roles(role6)
        await message.author.remove_roles(role7)
        time.sleep(1)
        await message.author.add_roles(role2)
        await message.channel.send(f"{message.author.mention} 변경 완료!")
        await message.author.send(f'{message.author.mention} 변경 완료!')
    if message.content.startswith("!노"):
        role1 = discord.utils.get(message.author.guild.roles, name="빨간색") #빨
        role2 = discord.utils.get(message.author.guild.roles, name="주황색") #주
        role3 = discord.utils.get(message.author.guild.roles, name="노란색") #노
        role4 = discord.utils.get(message.author.guild.roles, name="초록색") #초
        role5 = discord.utils.get(message.author.guild.roles, name="파란색") #파
        role6 = discord.utils.get(message.author.guild.roles, name="남색") #남
        role7 = discord.utils.get(message.author.guild.roles, name="보라색") #보
        await message.author.remove_roles(role2)
        await message.author.remove_roles(role1)
        await message.author.remove_roles(role4)
        await message.author.remove_roles(role5)
        await message.author.remove_roles(role6)
        await message.author.remove_roles(role7)
        time.sleep(1)
        await message.author.add_roles(role3)
        await message.channel.send(f"{message.author.mention} 변경 완료!")
        await message.author.send(f'{message.author.mention} 변경 완료!')
    if message.content.startswith("!초"):
        role1 = discord.utils.get(message.author.guild.roles, name="빨간색") #빨
        role2 = discord.utils.get(message.author.guild.roles, name="주황색") #주
        role3 = discord.utils.get(message.author.guild.roles, name="노란색") #노
        role4 = discord.utils.get(message.author.guild.roles, name="초록색") #초
        role5 = discord.utils.get(message.author.guild.roles, name="파란색") #파
        role6 = discord.utils.get(message.author.guild.roles, name="남색") #남
        role7 = discord.utils.get(message.author.guild.roles, name="보라색") #보
        await message.author.remove_roles(role2)
        await message.author.remove_roles(role1)
        await message.author.remove_roles(role3)
        await message.author.remove_roles(role5)
        await message.author.remove_roles(role6)
        await message.author.remove_roles(role7)
        time.sleep(1)
        await message.author.add_roles(role4)
        await message.channel.send(f"{message.author.mention} 변경 완료!")
        await message.author.send(f'{message.author.mention} 변경 완료!')
    if message.content.startswith("!파"):
        role1 = discord.utils.get(message.author.guild.roles, name="빨간색") #빨
        role2 = discord.utils.get(message.author.guild.roles, name="주황색") #주
        role3 = discord.utils.get(message.author.guild.roles, name="노란색") #노
        role4 = discord.utils.get(message.author.guild.roles, name="초록색") #초
        role5 = discord.utils.get(message.author.guild.roles, name="파란색") #파
        role6 = discord.utils.get(message.author.guild.roles, name="남색") #남
        role7 = discord.utils.get(message.author.guild.roles, name="보라색") #보
        await message.author.remove_roles(role2)
        await message.author.remove_roles(role1)
        await message.author.remove_roles(role3)
        await message.author.remove_roles(role4)
        await message.author.remove_roles(role6)
        await message.author.remove_roles(role7)
        time.sleep(1)
        await message.author.add_roles(role5)
        await message.channel.send(f"{message.author.mention} 변경 완료!")
        await message.author.send(f'{message.author.mention} 변경 완료!')
    if message.content.startswith("!남"):
        role1 = discord.utils.get(message.author.guild.roles, name="빨간색") #빨
        role2 = discord.utils.get(message.author.guild.roles, name="주황색") #주
        role3 = discord.utils.get(message.author.guild.roles, name="노란색") #노
        role4 = discord.utils.get(message.author.guild.roles, name="초록색") #초
        role5 = discord.utils.get(message.author.guild.roles, name="파란색") #파
        role6 = discord.utils.get(message.author.guild.roles, name="남색") #남
        role7 = discord.utils.get(message.author.guild.roles, name="보라색") #보
        await message.author.remove_roles(role2)
        await message.author.remove_roles(role1)
        await message.author.remove_roles(role3)
        await message.author.remove_roles(role4)
        await message.author.remove_roles(role5)
        await message.author.remove_roles(role7)
        time.sleep(1)
        await message.author.add_roles(role6)
        await message.channel.send(f"{message.author.mention} 변경 완료!")
        await message.author.send(f'{message.author.mention} 변경 완료!')
    if message.content.startswith("!보"):
        role1 = discord.utils.get(message.author.guild.roles, name="빨간색") #빨
        role2 = discord.utils.get(message.author.guild.roles, name="주황색") #주
        role3 = discord.utils.get(message.author.guild.roles, name="노란색") #노
        role4 = discord.utils.get(message.author.guild.roles, name="초록색") #초
        role5 = discord.utils.get(message.author.guild.roles, name="파란색") #파
        role6 = discord.utils.get(message.author.guild.roles, name="남색") #남
        role7 = discord.utils.get(message.author.guild.roles, name="보라색") #보
        await message.author.remove_roles(role2)
        await message.author.remove_roles(role1)
        await message.author.remove_roles(role3)
        await message.author.remove_roles(role4)
        await message.author.remove_roles(role5)
        await message.author.remove_roles(role6)
        time.sleep(1)
        await message.author.add_roles(role7)
        await message.channel.send(f"{message.author.mention} 변경 완료!")
        await message.author.send(f'{message.author.mention} 변경 완료!')
    if message.content.startswith("섹"):
        await message.channel.send(f"{message.author.mention} 스")
    if message.content.startswith("느"):
        await message.channel.send(f"{message.author.mention} 금마")
    if message.content.startswith("시"):
        await message.channel.send(f"{message.author.mention} 발")
    if message.content.startswith("씨"):
        await message.channel.send(f"{message.author.mention} 발")
    if message.content.startswith("야"):
        await message.channel.send(f"{message.author.mention} 뭐")
    if message.content.startswith("개"):
        await message.channel.send(f"{message.author.mention} 새끼")
    if message.content.startswith("sex"):
        await message.channel.send(f"{message.author.mention} mountain")

    global isPlaying, round, win, lose, firstLetter
    global who, lastWord, alreadySet, firstTurn, resetRound

    channel = message.channel

    if message.author.bot:
        return None

    if message.content in ['!끝말', '!끝말잇기', '!끝말카드']:
        if '!끝말' == message.content or '!끝말잇기' == message.content:
            embed = discord.Embed(title="끝말있기 채팅봇",
                                  description="Programmed by 월루")
            embed.add_field(name="시작", value="`!start` 또는 `!시작`", inline=True)
            embed.add_field(name="기권", value="`!exit`  또는 `!기권`", inline=True)
            embed.add_field(name="프로필 보기", value="`!끝말카드`", inline=False)
            await channel.send("", embed=embed)
        if message.content == "!끝말카드":
            if not (str(message.author.id) in user_card):
                user_card[str(message.author.id)] = {
                    "user": message.author.name,
                    "level": 1,
                    "word": 0,
                    "win": 0,
                    "length": 0
                }
            with open('user_info.json', 'w', encoding='utf-8') as file:
                file.write(json.dumps(user_card, ensure_ascii=False, indent=4))
            embed = discord.Embed(title=message.author.name,
                                  description=str(message.author.id))
            embed.add_field(name="레벨", value=str(user_card[str(message.author.id)]["level"]), inline=True)
            embed.add_field(name="승리", value=str(user_card[str(message.author.id)]["win"]), inline=True)
            embed.add_field(name="단어", value=str(user_card[str(message.author.id)]["word"]), inline=True)
            embed.add_field(name="글자", value=str(user_card[str(message.author.id)]["length"]), inline=True)
            await channel.send("", embed=embed)
    else:
        if message.channel.name == "끝말잇기":

            if not (str(message.author.id) in user_card):
                user_card[str(message.author.id)] = {
                    "user": message.author.name,
                    "level": 1,
                    "word": 0,
                    "win": 0,
                    "length": 0
                }
            else:
                patch_data(user_card[str(message.author.id)], "length", 0)

            with open('user_info.json', 'w', encoding='utf-8') as file:
                file.write(json.dumps(user_card, ensure_ascii=False, indent=4))

            if ('!start' == message.content or '!시작' == message.content) and (not isPlaying):
                round += 1
                if not (str(message.author.id) in user_card):
                    user_card[str(message.author.id)] = {
                        "user": message.author.name,
                        "level": 1,
                        "word": 0,
                        "win": 0
                    }
                    await channel.send(user_card.get(str(message.author.id)))
                    with open('user_info.json', 'w', encoding='utf-8') as file:
                        file.write(json.dumps(user_card, ensure_ascii=False, indent=4))

                embed = discord.Embed(title=str(round) + "라운드를 시작합니다. 현재 " + str(win) + "승 " + str(lose) + "패",
                                      description="기권하시려면 `!exit`  또는 `!기권`을 입력해주시기 바랍니다.")
                await channel.send("", embed=embed)

                lastWord = ''
                alreadySet = set()
                firstTurn, resetRound, isPlaying = True, False, True
                who = '성산봇'

            if isPlaying and who == '성산봇':
                if firstTurn:
                    lastWord = random.choice(list(wordDict[random.choice(list(wordDict.keys()))]))
                    alreadySet.add(lastWord)
                    await channel.send(' 성산봇 : ' + lastWord)
                    who = 'USER'
                    firstTurn = False

            if isPlaying and who == 'USER' and not message.author.bot and not firstTurn:
                yourWord = message.content
                if yourWord == '!exit' or yourWord == '!기권':
                    await channel.send('[결과] 당신은 기권했습니다. 성산봇의 승리입니다!')
                    resetRound = True
                    isPlaying = False
                    lose += 1
                    who = '성산봇'
                error = False

                firstLetter = yourWord[0]
                if (firstLetter != lastWord[-1]) and not checkDueum(lastWord[-1], firstLetter):
                    await channel.send(" [오류] '" + lastWord[-1] + "' (으)로 시작하는 단어를 입력하세요.")
                    who = 'USER'
                    error = True
                elif yourWord in hanbangSet:
                    await channel.send(' [오류] 한방단어는 사용할 수 없습니다.')
                    who = 'USER'
                    error = True
                elif yourWord in alreadySet:
                    await channel.send(' [오류] 이미 나온 단어입니다.')
                    who = 'USER'
                    error = True
                elif yourWord not in wordDict.get(firstLetter, set()):
                    await channel.send(' [오류] 사전에 없는 단어입니다.')
                    who = 'USER'
                    error = True

                if not error:
                    who = '성산봇'
                    alreadySet.add(yourWord)
                    lastWord = yourWord
                    user_card[str(message.author.id)]["word"] += 1
                    user_card[str(message.author.id)]["length"] += len(yourWord)
                    with open('user_info.json', 'w', encoding='utf-8') as file:
                        file.write(json.dumps(user_card, ensure_ascii=False, indent=4))
                    firstLetter = lastWord[-1]
                    if not list(filter(lambda x: x not in alreadySet, wordDict.get(firstLetter, set()))):
                        # 라운드 종료
                        await channel.send('[결과] 성산봇가 기권했습니다. 당신의 승리입니다!')
                        who = '성산봇'
                        isPlaying = False
                        win += 1
                        user_card[str(message.author.id)]["win"] += 1
                        with open('user_info.json', 'w', encoding='utf-8') as file:
                            file.write(json.dumps(user_card, ensure_ascii=False, indent=4))
                    else:
                        nextWords = sorted(filter(lambda x: x not in alreadySet, wordDict[firstLetter]),
                                           key=lambda x: -len(x))[
                                    :random.randint(20, 50)]
                        lastWord = nextWords[random.randint(0, random.randrange(0, len(nextWords)))]
                        alreadySet.add(lastWord)
                        await channel.send(' 성산봇 : ' + lastWord)
                        who = 'USER'

            if resetRound and not firstTurn:
                firstTurn, resetRound = True, False
                who = '성산봇'



with open('kkutu.txt', 'rt', encoding='utf-8') as f:
    s = f.read()

with open('user_info.json', 'r', encoding='utf-8') as file:
    user_info = json.load(file)
    user_card = user_info

with open('user_info.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(user_card, ensure_ascii=False, indent=4))

pat = re.compile('^[ㄱ-ㅎ가-힣]+$')
wordDict = dict()
hanbangSet = set()

for i in sorted([i for i in s.split() if pat.match(i) and len(i) >= 2], key=lambda x: -len(x)):
    if i[0] not in wordDict:
        wordDict[i[0]] = set()
    wordDict[i[0]].add(i)

delList = list()
for i in wordDict:
    for j in wordDict[i]:
        if j[-1] not in wordDict:
            delList.append(j)
for j in delList:
    hanbangSet.add(j)
    wordDict[j[0]].remove(j)



alreadySet = set()
round, win, lose = 0, 0, 0
who, lastWord, firstLetter = "성산봇", '', ''
firstTurn, resetRound, isPlaying = True, False, False


def patch_data(dict, null_name, null_data):
    if not (null_name in dict):
        dict[null_name] = null_data


def decompositeHangul(hangulLetter):
    cho_list = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
    jung_list = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'
    jong_list = ' ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ'

    hangulCode = ord(hangulLetter)
    cho_index = (hangulCode - 0xAC00) // 21 // 28
    jung_index = (hangulCode - 0xAC00 - (cho_index * 21 * 28)) // 28
    jong_index = hangulCode - 0xAC00 - (cho_index * 21 * 28) - (jung_index * 28)

    return (cho_list[cho_index], jung_list[jung_index], jong_list[jong_index])


def checkDueum(last_lastWord, first_yourWord):
    hangulRegex = re.compile("[가-힣]")
    if not pat.match(last_lastWord) and not pat.match(first_yourWord):
        return False

    lastWordDecompose = decompositeHangul(last_lastWord)
    yourWordDecompose = decompositeHangul(first_yourWord)

    if lastWordDecompose[0] in 'ㄴㄹ':
        if (lastWordDecompose[1] in 'ㅏㅐㅗㅚㅜㅡ') and lastWordDecompose[0] == 'ㄹ':
            if (yourWordDecompose[1:] == lastWordDecompose[1:]) and yourWordDecompose[0] == 'ㄴ':
                return True
            else:
                return False
        elif lastWordDecompose[1] in 'ㅑㅕㅛㅠㅣ':
            if (yourWordDecompose[1:] == lastWordDecompose[1:]) and yourWordDecompose[0] == 'ㅇ':
                return True
            else:
                return False
    else:
        return False


client.run("NjIyNDMyMzQ1OTE1NTIzMDk0.XrmhSw.bENuCr1vLUFxZj2wCndgnio2pYc")
