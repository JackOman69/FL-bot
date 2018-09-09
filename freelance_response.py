import requests
from bs4 import BeautifulSoup
from time import sleep

BASE_URL_FREELANCE_HUNT = "https://freelancehunt.com/projects"
BASE_URL_FL = "https://www.fl.ru/search/?type=projects&search_string=&action=search"


class Response():

    projects = []

    def __init__(self, response):
        self.name = response

    def get_html(self, url):
        resonse = requests.get(url)
        return resonse.text

    def get_dict(self):
        f_hunt = self.parse_freelanse_hunt(self.get_html(BASE_URL_FREELANCE_HUNT + "?name=" + self.name))
        f_fl = self.parse_fl(self.get_html(BASE_URL_FL + '&search_string=' + self.name))
        self.projects.extend(f_hunt)
        self.projects.extend(f_fl)
        return self.projects

    def parse_freelanse_hunt(self, html):
        try:
            soup = BeautifulSoup(html)
            table = soup.find('table', class_="table table-normal")

            sleep(0.15)
            project = []

            for rows in table.tbody.find_all('tr', class_=''):
                cols = rows.find_all('td')

                project.append({
                    'title': cols[0].a.text,
                    'category': [category.text for category in cols[0].div.find_all('small')],
                    'price': [price.text.strip() for price in
                              cols[1].span.find_all('div', class_="text-green price with-tooltip")],
                    'rates_num': cols[2].a.text,
                    'req': 'Не указано'
                })

            return project
        except:
            return []

    def parse_fl(self, html):
        try:
            soup = BeautifulSoup(html)
            content1 = soup.find_all('div', class_="search-lenta-item c ")
            project = []
            for content in content1:
                project.append({
                    'title': content.h3.a.text,
                    'category': self.name,
                    'price': [content.div.span.text],
                    'rates_num': content.div.div.span.a.text,
                    'req': content.p.text.strip()
                })

            return project
        except:
            return []
