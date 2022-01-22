import requests
from bs4 import BeautifulSoup
URL = "https://www.film.ru/news"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36", 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


a = []
start = 0
end = 2

b = []
href = []

box_for_info_text = []


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    artical_cards = soup.find_all("a", class_="topic")

    for items in artical_cards:
        artical_title = items.find("span")
        for elems in artical_title:
            if str(elems).find("strong") == True:
                pass
            else:
                if artical_title.index(elems) > 0:
                    a.append(f"<u>{elems}</u>")
                else:
                    a.append(f"{elems}")
        href.append("https://www.film.ru/" + items.get('href'))


def get_content_into(info_href):
    soup = BeautifulSoup(info_href, 'html.parser')
    info_text = soup.find('div', class_="text_2").get_text()
    box_for_info_text.append(info_text)


images = []


def get_image(img_href):
    soup = BeautifulSoup(img_href, 'html.parser')
    image_path = soup.find_all("div", class_="widescreen")
    for elems in image_path:
        image_href = elems.find_all('img')[0].get("src")
    # images_bytes = requests.get(image_href).content
    images.append(image_href)


def main(start, end):
    html = get_html(URL)
    info = get_content(html.text)
    for i in range(len(a)//3):
        b.append("".join(a[start:end]).upper())
        start += 2
        end += 2
        info_href = get_html(href[i])
        get_content_into(info_href.text)
        get_image(info_href.text)


main(start, end)
