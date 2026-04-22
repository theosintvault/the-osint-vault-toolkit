import requests
import requests

def check_username_sites(usernames):
    results = {}

    sites = {
        "github": "https://github.com/{}",
        "reddit": "https://www.reddit.com/user/{}",
        "twitter": "https://twitter.com/{}",
        "instagram": "https://www.instagram.com/{}",
        "tiktok": "https://www.tiktok.com/@{}",
        "medium": "https://medium.com/@{}",
        "pastebin": "https://pastebin.com/u/{}",
	"linkedin": "https://linkedin.com/@{}",
	"youtube": "https://youtube.com/@{}",
	"discord": "https://discord.com/@{}",
	"wechat": "https://wechat.com/@{}",
 	"telegram": "https://telegram.com/@{}",
	 "spotify": "https://spotify.com/@{}",
	"vimeo": "https://vimeo.com/{}",
	"tumblr": "https://tumblr.com/blog/{}",
	"snapchat": "https://snapchat.com/add/{}",
	"whatsapp": "https://wa.me/{}",
	"x": "https://x.com/{}",
	"bilibili": "https://bilibili.com/{}",
	"kuaishou": "https://kuaishou.com/profile/{}",
	"douyin": "https://douyin.com/@{}",
	"xiaohongshu": "https://xiaohongshu.com/user/{}",
	"weibo": "https://weibo.com/u/{}",
	"viber": "https://viber.com/{}",
	"line": "https://line.me/ti/p/~{}",
	"okru": "https://ok.ru/{}",
	"vk": "https://vk.com/{}",
	"dribbble": "https://dribbble.com/{}",
	"behance": "https://behance.net/{}"
    }

    for username in usernames:
        results[username] = {}

        for site, url in sites.items():
            try:
                r = requests.get(url.format(username), timeout=5)
                results[username][site] = (r.status_code == 200)
            except:
                results[username][site] = False
