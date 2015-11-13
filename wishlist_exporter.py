#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

output_dict = {}
page = 1

while page < 5:

    url = "http://www.amazon.com/gp/registry/wishlist/1FXKWNE64BY0H?ie=UTF8&page={}".format(page)

    parameters = {"q": ''.format(),
                  "num": ''.format()}

    headers = {'user-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

    r = requests.get(url,
                     params=parameters,
                     headers=headers)

    soup = BeautifulSoup(r.content, 'lxml', from_encoding='utf-8')
    # soup = BeautifulSoup(soup.text)

    # isolate li/g tags
    li_soup = soup.findAll('div', {"class": "a-row a-size-small"})

    for i in li_soup:

        div = i.get_text().strip()
        results = []

        for item in div.split('\n'):

            if item.strip():

                results.append(item.replace('by ', '').replace('(Hardcover)', '').replace('(Paperback)', '').strip())

            else:

                continue

        output_dict[results[1]] = results[0]

    page += 1

output_file = 'wish_list.html'

with open(output_file, 'wb') as outfile:

    formatting = """
\t\t<strong><dt>{author} -</strong></dt>
\t\t<br />

\t\t\t\t<dd>{title}</dd>

\t\t<br />
    """
    for k, v in output_dict.iteritems():

        outfile.write(formatting.format(author=k, title=v))
