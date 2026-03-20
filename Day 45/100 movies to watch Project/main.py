import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')
print(soup.original_encoding)
hundred_movies = [title.getText() for title in soup.find_all(name='h3', class_='title')]
# print(hundred_movies) #the list is out of order

final_list = hundred_movies[::-1] #reverses the list

#prints the list
print("The 100 Greatest Movies")
for movie in final_list:
    print(movie)

#save a file with the list
with open('movies.txt', mode='w', encoding='utf-8') as file:

    for movie in final_list:
        file.write(f"{movie}\n")
