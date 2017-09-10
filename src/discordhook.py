import requests

class Client:

    def __init__(self, url, **kwargs):
        # URL to the Webhook, should be provided by Discord. (required)
        self.url = url

        # The message contents (up to 2000 characters), required if no embed.
        self.message = kwargs.get('message')
        
        # Override the default username of the webhook, optional.
        self.name = kwargs.get('name')

        # Override the default avatar of the webhook, optional.
        self.avatar_url = kwargs.get('avatar_url')

        # True if this is a TTS message, optional.
        self.tts = kwargs.get('tts')

        # Embedded rich content, required if no message.
        self.embed = kwargs.get('embed')

    def send(self):
        
        data = {'content': self.message,
                'username': self.name,
                'avatar_url': self.avatar_url,
                'tts': self.tts,
                'embeds': [self.embed] if self.embed else None
                }
        r = requests.post(self.url, json=data)
        if r.status_code != 204:
            raise Exception('HTTP Error: Status Code {}'.format(r.status_code))
        else:
            return True
