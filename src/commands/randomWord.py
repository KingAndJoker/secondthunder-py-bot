import random
import asyncio
from src.libs.dataImport import dataImport
from src.libs.getRandomUser import getRandomUser
from src.libs.databaseHandler import getDataFromDatabase, editDataInDatabase
wordsArray = dataImport('src/data/words.txt')
delayTime = 3


async def randomWord(msg, args):
    if len(args) == 0:
        currentUser = msg.author.mention
    elif args[0] == 'рандом':
        randomUser = await getRandomUser(msg)
        currentUser = randomUser.mention
    else:
        currentUser = args[0]
    isSpamTriggerEnabled = spamChecker(msg)
    if isSpamTriggerEnabled:
        await msg.channel.send(f'{msg.author.mention} куда спамиш?', delete_after=delayTime)
        await asyncio.sleep(delayTime)
        await msg.delete()
    else:
        await msg.channel.send(f'{currentUser} {random.choice(wordsArray)}')


def spamChecker(msg):
    currentStatus = getDataFromDatabase('variables', ['spammerID', 'spammerCount'])
    if currentStatus[0] == msg.author.id:
        if currentStatus[1] >= 3:
            editDataInDatabase('variables', ['spammerCount'], [0])
            return True
        editDataInDatabase('variables', ['spammerCount'], [currentStatus[1] + 1])
        return False
    editDataInDatabase('variables', ['spammerID', 'spammerCount'], [msg.author.id, 1])
    return False
