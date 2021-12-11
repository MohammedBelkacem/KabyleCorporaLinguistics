# -------------------------------------------------------------------------------
# Name:        Linguistics corpora construction
# Purpose:     NLP use
#
# Author:      Mohammed Belkacem
#
# Created:     10/12/2021
# Copyright:   (c) Mohammed Belkacem 2021
# Licence:     CCO
# -------------------------------------------------------------------------------

## This script creates text file for each article
## Files are utf-8 encoded
## This script is for nlp use only
## This script can't be used on other websites. If this website is updated, it may not work
## Dont forget to cite me

from requests_html import HTMLSession
import re
import os
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


categories = ['regions','sport', 'societe', 'culture',  'sante-science-technologie','algerie', 'economie', 'monde']
taille = [192, 166, 144, 162,  138, 710, 232, 207]

# Nmber of all pages. Please look at the number dispyed on the web site at
# https://www.depechedekabylie.com/ddk-tamazight/ if the max pages is 690; please change it above to 684
all_pages = 684
# number of retrieved pages. Please change it. Note that  it takes a lot of time to fetch articles
max_pages = 3


# construct pages urls

def retreive_pages(categories, taille):
    pages = []
    for i in categories:
        #print(taille[categories.index(i)] * 10)

        for j in range(taille[categories.index(i)]):
            pages.append('https://www.aps.dz/tamazight-tal/' + i + "?start=" + str(j * 10))  # first page
        print(pages)
        #exit()

    return pages


# remove html tags from content
def remove_tags(text, TAG_RE):
    return TAG_RE.sub('', text)


# create articles retreived from a page
def create_article(article, a):
    TAG_RE = re.compile(r'<[^>]+>')
    session = HTMLSession()
    article = 'https://www.aps.dz' + article
    print (article)
    time.sleep(10)
    try:
        if not os.path.isfile(str(a) + ".txt"):
            r = session.get(article, verify=False,proxies={"http": "http://111.233.225.166:1234"})
            about = r.html.find('p')
            g = open(str(a) + ".txt", "w+", encoding='utf-8')

            for i in about:
                #print (remove_tags(i.html, TAG_RE))

                g.write(remove_tags(i.html, TAG_RE) + '\n')
            g.close()
    except:
        print(article)


def fetch_pages(max_pages, all_pages, categories, taille):
    articles = []
    nb_page = 0
    session = HTMLSession()
    a = 0
    for page in retreive_pages(categories, taille):
        time.sleep(10)
        try:
            r = session.get(page, verify=False,proxies={"http": "http://111.233.225.166:1234"})

            about = r.html.find('a')


            for i in about:

                if i.html.find('href="/tamazight-tal/algerie/') > 0 \
                        or i.html.find('href="/tamazight-tal/economie/') > 0 \
                        or i.html.find('href="/tamazight-tal/monde/') > 0 \
                        or i.html.find('href="/tamazight-tal/sport/') > 0 \
                        or i.html.find('href="/tamazight-tal/societe/') > 0 \
                        or i.html.find('href="/tamazight-tal/culture/') > 0 \
                        or i.html.find('href="/tamazight-tal/regions/') > 0 \
                        or i.html.find('href="/tamazight-tal/sante-science-technologie/') > 0:  # and #i.html.find('rel="bookmark" class="td-image-wrap"') > 0:

                    j = i.html.split(' ')[1].split('"')[1]
                    if j not in articles:
                        articles.append(j)
                        create_article(j, a)
                        a = a + 1

            nb_page = nb_page + 1
        except:
            print(page)

fetch_pages(max_pages, all_pages, categories, taille)
