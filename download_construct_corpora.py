#-------------------------------------------------------------------------------
# Name:        Linguistics corpora construction
# Purpose:     NLP use
#
# Author:      Mohammed Belkacem
#
# Created:     10/12/2021
# Copyright:   (c) Mohammed Belkacem 2021
# Licence:     CCO
#-------------------------------------------------------------------------------

## This script creates text file for each article la dépèche de Kabylie
## Files are utf-8 encoded
## This script is for nlp use only
## This script can't be used on other websites. If this website is updated, it may not work
## Dont forget to cite me

from requests_html import HTMLSession
import re

#Nmber of all pages. Please look at the number dispyed on the web site at https://www.depechedekabylie.com/ddk-tamazight/
#if the max pages is 690; please change it abouve to 684
all_pages=684
#number of retrived pages. Please change it. Note that  it takes a lot of time to fetcth artiles
max_pages=2

#construct pages urls
def retreive_pages(all_pages):
    pages=['https://www.depechedekabylie.com/ddk-tamazight/']#first page
     #remaining pages
    for i in range (all_pages):
        pages.append(pages[0]+"page/"+str(i+1)+"/") #link to pages
    return pages
#remove html tags from content
def remove_tags(text,TAG_RE):

    return TAG_RE.sub('', text)
#create articles retreived from a page
def create_article (article,a ):
        TAG_RE = re.compile(r'<[^>]+>')
        session = HTMLSession()

        r = session.get(article)

        about = r.html.find('p')
        g=open(str(a)+".txt","w+",encoding='utf-8')

        for i in about:
             g.write(remove_tags(i.html,TAG_RE)+'\n')
        g.close()


def fetch_pages (max_pages,all_pages):
    articles=[]
    nb_page=0
    session = HTMLSession()
    a=0
    for page in retreive_pages(all_pages):
     r = session.get(page)

     about = r.html.find('a')

     for i in about:
        if i.html.find('https://www.depechedekabylie.com/ddk-tamazight/')>0 and i.html.find('rel="bookmark" class="td-image-wrap"')>0:
             j=i.html.split(' ')[1].split('"')[1]
             if j not in articles:
                articles.append(j)
                create_article(j,a)
                a=a+1
     nb_page=nb_page+1
     if nb_page==max_pages:
        break

fetch_pages (max_pages,all_pages)
