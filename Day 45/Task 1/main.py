# introduction to beautiful soup documentation in: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup # importing beautiful soup 4



with open('website.html', 'r') as f: # the website.html file was sourced from the course
    website = f.read()

soup = BeautifulSoup(website, 'html.parser')
print(soup.title) # should print the <title> content of the html page
print(soup.title.string) # should print the content of the title tag
print(soup.a) # will print the first <a> tag if you add a tag that can be repeated on the page, it will give the first one

all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags) #it will print all the <a> tags in the document

for tag in all_anchor_tags:
    print(tag.get("href")) #it will print all the href (links) in the <a> tags

heading = soup.find(name='h1', id='name')
print(heading) #it will print the isolated h1 with the id 'name'

section_heading = soup.find(name='h3', class_='heading') #the class_ is used to not clash with the reserved python word
print(section_heading)
print(section_heading.name) #gets the name of the tag
print(section_heading.getText())  #gets the content of the tag
print(section_heading.get('class')) #gets value of the attribute 'class' of the tag

#css selector

company_url = soup.select_one(selector="p a") #selects the <p><a> tag
print(company_url)
name = soup.select_one(selector="#name") #selects the element with the id 'name'
print(name)