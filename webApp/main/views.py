from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
import requests
from .models import Word

import fake_useragent
from bs4 import BeautifulSoup


def index(request):
    words = Word.objects.all()
    return render(request, 'main/index.html', {"words": words, "i":1})
    pass

def update(request):
    words = updateWords()
    for i in range(len(words)):
        Word.objects.get_or_create(eng=words[i]["word"], ru=words[i]["trans"])
        pass
    return HttpResponseRedirect(f"/")
    pass








def updateWords():
    session = requests.Session()
    link = "https://puzzle-movies.com/api2/user/exists?callback=jQuery1113038188034758527434_1654011898534"
    user = fake_useragent.UserAgent().random

    header = {
        'user-agent': user
    }

    data = {
        'email': 'artem.k3001@gmail.com',
    }

    response = session.post(link, data=data, headers=header).text

    link = "https://puzzle-movies.com/api2/user/signin?redirect_to=%2Fuser"

    data = {
        'email': 'artem.k3001@gmail.com',
        'password': 'Artemk2001'
    }

    response1 = session.post(link, data=data, headers=header).text

    index = session.get("https://puzzle-movies.com/dictionary", headers=header)

    soup = BeautifulSoup(index.text, 'lxml')
    all_piece = soup.find_all(
        "div", class_="dict__video__list-table__word__main movies-text_style_eee puzzle-text_fz_18 translate_line_without_popup")
    words = []

    for piece in all_piece:
        w = piece.find("span", class_="balloon-row").text
        w = w.replace(" ", "").replace("\n", "")
        try:
            w = piece.find(
                "span", class_="dict__video__list-table__word__main__article").text + ' ' + w
        except:
            pass

        json = {
            "word": f"{w}",
            "trans": f"{piece.find('span', class_='balloon-row').attrs['data-translation']}"
        }
        words.append(json)
    return words



