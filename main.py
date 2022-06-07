import os
import requests
from bs4 import BeautifulSoup


os.makedirs('mazhar khaleghi', exist_ok=True)
os.makedirs('musics', exist_ok=True)

URLS = ["https://musickordi.com/full-album/%D9%85%D8%B8%D9%87%D8%B1-%D8%AE%D8%A7%D9%84%D9%82%DB%8C/",
       "https://musickordi.com/music/9319/%D8%A8%D8%B2%D8%B1%DA%AF%D8%AA%D8%B1%DB%8C%D9%86-%DA%AF%D9%84%DA%86%DB%8C%D9%86-%D8%A2%D9%87%D9%86%DA%AF%D9%87%D8%A7%DB%8C-%DA%A9%D8%B1%D8%AF%DB%8C-%D9%82%D8%AF%DB%8C%D9%85%DB%8C/"]
# input the album number
URL = "".join(URLS[int(input(
    "Which album do you want to download?\n 1. The album of the Mazhari khaleghi\n 2. The album of the Kurdish General Signers\n"))-1])

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
list_of_musics = soup.find_all('a', class_='download-link-btn')
for music in list_of_musics:
    try:
        print(requests.head(music['href']).headers)
        music_url = music.get('href')
        if music_url.split('/')[-1] not in os.listdir('musics'):
            print(music_url)
            with open(f"mazhar khaleghi/{music_url.split('/')[-1]}", 'wb') as f:
                f.write(requests.get(music_url).content)
    except:
        print('error ---------------------------------------------------------------------------------------------------------------------')
