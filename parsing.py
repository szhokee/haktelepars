import requests
from bs4 import BeautifulSoup as BS


def get_html(url):
    response = requests.get(url)
    return response.text


def get_soup(html):
    soup = BS(html, 'lxml')
    return soup


def get_data(soup):
    news = soup.find_all('div', class_='Tag--article')
    data = []

    count_ = 0

    for i in news:
        title = i.find('a', class_='ArticleItem--name').text.strip()
        photo = i.find('img').get('src')
        # print(title)
        description_url = i.find('a', class_='ArticleItem--name').get('href')
        # print(description_url)
        description_html = get_html(description_url)
        description_soup = get_soup(description_html)
        # description = description_soup.find('div', class_='')
        description = description_soup.find('div', class_='BbCode').text.replace('\n', '')
        # print(description)

        data.append([title, photo, description])
        
        count_ += 1
        if count_ == 20:
            break

        # print(data)
        # break
    return data    



def main():
    url = 'https://kaktus.media/?lable=8&date=2022-12-22&order=time'
    html = get_html(url)
    soup = get_soup(html)
    date = get_data(soup)
    return date

# print(main())
# main()





