# -*- coding: utf-8 -*-
"""Web Scrapping Beautiful soup.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EZnDWGr0gNj6Drmkgw9wpM3PaZacK3W3

### Searching the tree

---



---
"""

from bs4 import BeautifulSoup

htmldoc='/content/EdYoda _ Jobs.html'
with open(htmldoc,'r') as edyoda:
  soup=BeautifulSoup(edyoda,'lxml')

type(soup)

soup.contents

tag_li=soup.find('li')

type(tag_li)



import re
email_ex='''<br/>
<p/>testng diff email stuff using regular exp<p/>
vinu@gmail.com
kk@gmail.com
vv@gmail.com 
'''

soup=BeautifulSoup(email_ex,'lxml')
email_regex=re.compile('\w+@\w+\.\w+')

soup.contents

id=soup.find_all(text=email_regex)

id

book_html_doc="""
  <catalog>
  <head><title>The web book catalog </title> </head>
  <p class="title"><b>The Book Catalog</b></p>
  <books>
  <book id="bk001">
  <author>Hightower, Kim</author>
  <title>The First Book</title>
    <genre Fiction</genre>
    <price>44.95</price> <pub_date>2000-10-01</pub_date>
    <review>An amazing story of nothing.</review>
  </book>
  <book id="bk002">
    <author>Nagata, Suanne</author>
    <title>Becoming Somebody</title>
    <genre>Biography</genre>
    <review>A masterpiece of the fine art of gossiping.</review>
  </book>
  <book id="bk003">
    <author>Oberg, Bruce</author>
    <title>The Poet's First Poem</title>
    <genre>Poem</genre>
    <price>24.95</price>
    <review>The least poetic poems of the decade.</review> 
  </book> </books></catalog>"""

soup=BeautifulSoup(book_html_doc, 'html.parser')
soup.contents

print(soup.catalog)

soup.head

title_tag=soup.title
title_tag

soup.catalog.p

for i in soup.descendants:
  print(i)

for i in soup.head.descendants:
  print (i)

for string in soup.stripped_strings:
  print(string)

title_tag.parent

title_tag.parent

element_soup=soup.catalog.books
print(element_soup)

next_element=element_soup.next_element.next_element
next_element

previous_element=next_element.previous_element.previous_element
previous_element

next_sibling=soup.catalog.books.book
next_sibling

next_sibling2=next_sibling.next_sibling
next_sibling2.next_sibling

previous_sibling=next_sibling2.previous_sibling
previous_sibling

"""### Modifying tree"""

from bs4 import BeautifulSoup

#Create employee html document 
employee_html_doc="""<employees>
  <employee class="accountant">
    <firstName>John</firstName> <lastName>Doe</lastName>
  </employee>
  <employee class="manager">
    <firstName>Anna</FirstName> <lastName>Smith</lastName>
  </employee>
  <employee class="developer">
    <firstName>Peter</firstName> <lastName>Jones</lastName>
  </employee>
</employees>"""

soup=BeautifulSoup(employee_html_doc, 'html.parser')

soup.employees

tag=soup.employee
tag

# modifying a tag

tag['class']='manager'

tag

# adding a new tag
tag=soup.new_tag('rank')
tag.string='new tag rank is inserted'

soup.employees.insert_after(tag)

soup.contents

tag.clear()

print(soup)

soup.employees.employee.insert_after(tag)

print(soup)

tag.clear()  # to clear the last modification

tag=soup.employees.employee

tag.firstname.string.extract()

tag.firstname.replace_with('Vinu')
tag

soup

"""### soupstrainer. Parsing parts of the document"""

from bs4 import BeautifulSoup

#sample web document from www.simplilearn.com website 
data_SL = """<ul class="content-col_discover">
  <h5>Discover</h5>
  <li><a href="/resources" id="free_resources">Free resources</a></li>
  <li><a href="http://community.simplilearn.com/" id="community">Simplilearn community</a></li>
  <li><a href="/career-data-labs" id="lab">Career data labs</a></li>
  <li><a href="/scholarships-for-veterans" id="scholarship">Veterans scholarship</a></li>
  <li><a href="http://www.simplilearn.com/feed/" id="rss">RSS feed</a></li>
</ul>"""

soup=BeautifulSoup(data_SL,'html.parser')

print(soup.get_text())

from bs4 import SoupStrainer

tags_with_lablink=SoupStrainer(id='lab')
soup=(BeautifulSoup(data_SL,'html.parser',parse_only=tags_with_lablink).prettify())

print(soup)

print(soup.get_text())

"""### Output- printing and formating"""

from bs4 import BeautifulSoup
import requests

url='https://www.simplilearn.com/'

results=requests.get(url)
webpage=results.content
soup=BeautifulSoup(webpage, 'html.parser')

soup.contents

print(soup.prettify())

#view original encoding

soup.original_encoding

# formating a tag to xml

soup.body.a.prettify(formatter='xml')

#define a custom function to convert string values to uppercase
def uppercase(string):
  return string.upper()

soup.body.a.prettify(formatter=uppercase)

"""### encoding"""

from bs4 import BeautifulSoup
import requests

url='https://www.simplilearn.com/'

results=requests.get(url)
presoup=results.content
soup=BeautifulSoup(presoup, 'html.parser')

# closing results object
results.close()

soup.contents

#prettify

print(soup.prettify())

soup.head

soup.title

for link in soup.findAll('a',href=True):
  print(link['href'])



"""### Web Scrapping"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

url='https://www.simplilearn.com/'
request=urlopen(url)
soup=BeautifulSoup(request,'html.parser')
request.close()

soup.contents

print(soup.prettify())

soup.head

soup.title

for link in soup.findAll('a',href=True):
  print(link['href'])

for article in soup.findAll('h2'):
  print(article.string)

for article in soup.findAll('h2'):
  print(article)

for article in soup.findAll('h3'):
  print(article.string)

for article in soup.findAll('h4'):
  print(article.string)

url2='https://www.simplilearn.com/tutorials/project-management-tutorial/what-is-agile-project-management?source=frs_home'
url2web=urlopen(url2)
soup2=BeautifulSoup(url2web,'html.parser')
test=soup2.find(class_='desig_author empty-text')

soup.contents

print(soup2.prettify())

type(test)

test.findAll('p')

first_next=test.p
first_next

find_next_sibling=first_next.next_sibling.next_sibling
find_next_sibling

find_previous_sibling=find_next_sibling.previous_sibling.previous_sibling
find_previous_sibling

