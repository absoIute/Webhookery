import requests

class Client:

    def __init__(self, url):
        # URL to the Webhook, should be provided by Discord. (required)
        self.url = url

        # The message contents (up to 2000 characters), required if no embed.
        self.message = None
        
        # Override the default username of the webhook, optional.
        self.name = None

        # Override the default avatar of the webhook, optional.
        self.avatar_url = None

        # True if this is a TTS message, optional.
        self.tts = None

        # Embedded rich content, required if no message.
        self.embed = None

    def send(self):
        
        data = {'content': self.message,
                'username': self.name,
                'avatar_url': self.avatar_url,
                'tts': self.tts,
                'embeds': [self.embed]
                }
        r = requests.post(self.url, json=data)
        if r.status_code != 204:
            raise Exception('HTTP Error: Status Code {}'.format(r.status_code))
        else:
            return True
