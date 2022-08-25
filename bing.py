import requests
import get_center
from rich import print

def get_list(list_text, start = 0):
    if list_text.find('<div class="b_title">', start) != -1:
        return [get_center.get(list_text, '<h2>', "</h2>", list_text.find('<div class="b_title">', start))] + get_list(list_text, list_text.find('<div class="b_title">',start) + 15)
    else:
        return []

def get_url(html):
    url = get_center.get(html, "href=\"", '"')
    title = get_center.get(html, ">", "</a>")
    title = title.replace("<strong>", "")
    title = title.replace("</strong>", "")
    return [title, url]

def search(keyword,page = "1"):
    req = requests.get("https://cn.bing.com/search?q=" + keyword + "&first=" + page)
    html = req.text
    list_text = get_center.get(html, '<ol id="b_results" class="">', "</ol>")
    html_list = get_list(list_text)
    
    search_list = []
    for h in html_list:
        search_list += [get_url(h)]
    return search_list
    # print(search_list)

if __name__ == "__main__":
    keyword = input("Search: ")
    s = search(keyword)

    len = 0
    # print(s)
    for i in s:
        len += 1
        print(f"{len}. {i[0]}\n  [green]{i[1]}[/]")
