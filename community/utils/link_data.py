import requests
import json
from lxml import html


class LinkData():

    def __init__(self, url_group):
        self.url_group = url_group
        self.headers = {
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40',
        }

    def get_data(self):
        raw_response = requests.get(self.url_group, headers=self.headers)
        html_response = html.fromstring(raw_response.text)
        name = html_response.xpath('//meta[@property="og:title"]/@content')
        # name = []
        if not name:
            print('title name')
            name = html_response.xpath('//title/text()')
        description = html_response.xpath(
            '//meta[@property="og:description"]/@content')
        if not description:
            description = html_response.xpath(
                '(//body/div[contains(@class, "container")]//p/text())[0]')
            if not description:
                description = html_response.xpath(
                    '//div[contains(@class, "container")]//p/text()')
        else:
            description = description[0]

        image = html_response.xpath(
            '//meta[@property="og:image"]/@content')
        if not image:
            image = html_response.xpath(
                '//img/@src')
        data = {
            'name': name[0],
            'description': description
        }
        return data


# url_test = 'https://www.python.org/'
# url_test = 'https://www.php.net/'
url_test = 'https://www.djangoproject.com/'
geturl = LinkData(url_test)
response = geturl.get_data()
print(response)
