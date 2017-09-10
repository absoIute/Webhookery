# DiscordPyHook
Very lightweight Discord Webhook wrapper written in Python
## Getting Started
Move the [discordhook.py](discordhook.py) file into your Python directory and install the requests python package through pip: `pip install requests` or `pip install -r requirements.txt`

## Creating a Webhook
1) Navigate to the __Webhooks__ page in server settings and click __Create Webhook__.

![](https://image.prntscr.com/image/_Hly1DCeRT6JeeLLDyVVkQ.png)
2) Copy the Webhook url

![](https://image.prntscr.com/image/SjNR5kt_QR_Z-9HLXjW4ug.png)

## Sending Messages
Sending messages though the Webhook is simple, declare your Webhook using `discordhook.Client(...)` and send a message with `discordhook.Client.send()`!

Plain Text:
```py
import discordhook

hook = discordhook.Client('Webhook URL',
                          message='Hello World',
                          name='My WebHook',
                          avatar_url='Image URL')
hook.send()
```

## Sending Rich Embeds
To send Rich Embeds though your Webhook, you will need to install the [discord.py](https://github.com/Rapptz/discord.py/) module, to do this just run `pip install discord.py`, then you can use the `discord.Embed` object! Note: you will need to convert the embed to a dict using `discord.Embed.to_dict()`.
```py
import discordhook
import discord  # discord.py

hook = discordhook.Client('Webhook URL',
                          embed=discord.Embed(description='Hello World').to_dict(),
                          name='My WebHook',
                          avatar_url='Image URL')
hook.send()
```
