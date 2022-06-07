import os
import requests
from bs4 import BeautifulSoup


os.makedirs('musics', exist_ok=True)
response= requests.get("https://musickordi.com/music/9319/%D8%A8%D8%B2%D8%B1%DA%AF%D8%AA%D8%B1%DB%8C%D9%86-%DA%AF%D9%84%DA%86%DB%8C%D9%86-%D8%A2%D9%87%D9%86%DA%AF%D9%87%D8%A7%DB%8C-%DA%A9%D8%B1%D8%AF%DB%8C-%D9%82%D8%AF%DB%8C%D9%85%DB%8C/")
soup = BeautifulSoup(response.text, 'html.parser')
list_of_musics=soup.find_all('a',class_='download-link-btn')
for music in list_of_musics:
    try:
        music_url=music.get('href')
        print(music_url)
        with open(f"musics/{music_url.split('/')[-1]}", 'wb') as f:
            f.write(requests.get(music_url).content)
    except:
        print(music.get('href'))
        continue