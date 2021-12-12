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

## This script creates text file for each article
## Files are utf-8 encoded
## This script is for nlp use only
## This script can't be used on other websites. If this website is updated, it may not work
## Dont forget to cite me

from requests_html import HTMLSession
import re

#Nmber of all pages. Please look at the number dispyed on the web site at http://isahliyen.com/
#if the max pages is 690; please change it abouve to 684
all_pages=684
#number of retrived pages. Please change it. Note that  it takes a lot of time to fetcth artiles
max_pages=2

#construct pages urls
def retreive_pages(all_pages):
    pages=['http://isahliyen.com/','http://isahliyen.com/category/actualite/','http://isahliyen.com/category/addal/','http://isahliyen.com/category/chanson-kabyle/',
    'http://isahliyen.com/category/contributions/','http://isahliyen.com/category/idles/','http://isahliyen.com/category/kabylie/','http://isahliyen.com/category/monde/',
    'http://isahliyen.com/category/non-classe/','http://isahliyen.com/category/sante/','http://isahliyen.com/category/science/','http://isahliyen.com/category/solidarite-kabyle/',
    'http://isahliyen.com/category/taddart/','http://isahliyen.com/category/tasekla/','http://isahliyen.com/category/tayri/','http://isahliyen.com/category/technologie/',
    'http://isahliyen.com/category/tidiwenniyin/','http://isahliyen.com/category/tine%e1%b8%8druyin/','http://isahliyen.com/category/top-10/','http://isahliyen.com/category/villages-kabyles/']#first page
     #remaining pages
    return pages
#remove html tags from content
def remove_tags(text,TAG_RE):

    return TAG_RE.sub('', text)
#create articles retreived from a page
def create_article (article,a ):

        TAG_RE = re.compile(r'<[^>]+>')
        session = HTMLSession()
        try:
         r = session.get(article)

         about = r.html.find('p')
         g=open(str(a)+".txt","w+",encoding='utf-8')

         for i in about:
             g.write(remove_tags(i.html,TAG_RE)+'\n')
         g.close()
        except :
            print(article)


def fetch_pages (max_pages,all_pages):
    articles=[]
    nb_page=0
    session = HTMLSession()
    a=0
    for page in retreive_pages(all_pages):
     r = session.get(page)

     about = r.html.find('a')

     for i in about:

        #print(i)
        if i.html.find('http://isahliyen.com/20')>0 :
            article=i.html.split(" ")[1].split('"')[1]
            if article  not in articles:
                articles.append(article)
                create_article (article,a )
                a=a+1


fetch_pages (all_pages,all_pages)
print ("fin")
