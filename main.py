import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

movie_list = soup.find_all(name="h3", class_="title")
movie_name = [movies.getText() for movies in movie_list]
sorted_movie_list = movie_name[::-1]

for movie in sorted_movie_list:
    with open("movies.txt", "a", encoding="utf-8") as file:
        file.write(f"{movie}\n")