from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests
from time import sleep
import re

# Create your views here.

def fetch_data_from_tr(request):
    movie_links_list = []

    for i in range(20):
        sleep(1)
        movies_list_url = (f"https://www.tamilrockermovies.vip/movies/page/{i}/")
        req_site = requests.get(movies_list_url)
        beautify = bs(req_site.text, 'html.parser')

        link_list = beautify.find_all("article")
        for j in link_list:
            movie_single_link = j.find('a').get('href')
            # add link to list

            #     url = 'https://www.tamilrockermovies.vip/watch-suvarna-purushan-online/'

            req_site = requests.get(movie_single_link)
            beautify = bs(req_site.text, 'html.parser')

            # Title
            pre_Movie_title = beautify.find(class_="site-content").find('h1').get_text()
            Movie_title = re.sub('\s+', '', pre_Movie_title)
            print(f'Title: {Movie_title}')

            # image
            pre_image_link = beautify.find(class_="movie-thumbnail-post-page").get('style')
            Image_link = re.split('[()]', pre_image_link)[1]
            print(f'Image Link: {Image_link}')

            # info
            pre_movie_info = beautify.find(class_="movie-info").get_text()
            print(pre_movie_info)

            # Media
            media = beautify.find_all(class_="movie-post-title")[2].find('a').get('href')
            print(f'Media: {media}')
            print('-\n\n\n-')

            movie_links_list.append(movie_single_link)


    return render(request, 'home.html')