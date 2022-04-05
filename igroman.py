import requests
from bs4 import BeautifulSoup

URL = "https://www.igromania.ru/kino/"
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_paage_id(html):

    soup = BeautifulSoup(html, 'lxml')
    pageID = soup.find_all('a', class_='aubli_name')[0:5]
    listId = set()
    for i in pageID:
        listId.add("https://www.igromania.ru/news/" +
                   i.get('href').split('/')[2] + "/")
    return listId


def get_title(url):
    soup = BeautifulSoup(url,"lxml")
    title = soup.find_all("h1",class_ = "page_news_ttl haveselect")
    return title

def get_page_text(url):
    soup = BeautifulSoup(url,"lxml")
    text = soup.find_all("div",class_ = "universal_content clearfix")
    stop = text[0].get_text().find("Больше на Игромании")
    return text[0].get_text()[0:stop-6].strip()
def get_image(url):
    soup = BeautifulSoup(url,'html.parser')
    found_image = soup.find_all('div', class_ = 'main_pic_container')
    for found in found_image:
        found = found.find_all('img')[0].get('src')
    return found

def get_all_info():
    html = get_html(URL)
    title = get_paage_id(html.text)
    all_info = []
    for site in title:
        all_info.append({
            "img":get_image(get_html(site).text),
            "title":get_title(get_html(site).text)[0].get_text(),
            "text":get_page_text(get_html(site).text).strip(),
            })
    return all_info

if __name__ == "__main__":
    get_all_info()()
