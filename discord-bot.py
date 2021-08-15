import discord

hello_words = ['hello', 'hi', 'good morning', 'good afternoon', 'good evening', 'hey', 'how are you?', 'how are you doing?']
info_words = ['how to make', 'help', 'please help', 'support', 'assist', 'problem']


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    msg_list = msg.split()

    #if msg in hello_words or len(list(set(msg_list + hello_words))) < len (msg_list) + len (hello_words):
    find_hello_words = False
    for item in hello_words:
        if msg.find(item) >= 0:
            find_hello_words = True
    if (find_hello_words):
        await message.channel.send('Hello! How can we help?')

    #if msg in info_words or len(list(set(msg_list + info_words))) < len (msg_list) + len (info_words):
    find_info_words = False
    for item in info_words:
        if msg.find(item)>=0:
            find_info_words = True
    if (find_info_words):
            await message.channel.send('Thank you for your contact. Your request is sent to the support team.')

        #print(msg_list)
        #print(hello_words)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$hi'):
        await message.channel.send(f' {message.author.mention} Hi!')

client.run('ODc0NTYyOTM0ODA0NzI1Nzcw.YRIyNA.P9zanrMUiPbcevw0tORed9LjkyI')
