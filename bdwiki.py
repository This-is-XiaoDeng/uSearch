import requests
import json

def search(keyword):
    req = requests.get("https://api.muxiaoguo.cn/api/Baike?api_key=a9f05a26ee2778e2&type=Baidu&word=" + keyword)
    data = json.loads(req.text)
    if data["code"] == 200:
        return data["data"]["content"]
    else:
        return None

if __name__ == "__main__":
    print(search(input("Search: ")))
