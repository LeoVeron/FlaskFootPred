import requests
import re
from requests import get
from bs4 import BeautifulSoup
from . import db
from .models import Upcoming_matches

BASE_URL = "https://www.soccerstats.com/"

def complete_matches():
    #Request
    league = 'france'
    response = requests.get(
        BASE_URL + 'results.asp',
        params={'league': league}
        )

    #Soup
    soup = BeautifulSoup(response.text, "html.parser")

    scores = soup.find_all(text=re.compile('h2h'))
    divs = [score.parent.parent.parent for score in scores]

    names = [dvs.text.replace('\xa0', ' ').replace('h2h', '') for dvs in divs],
    urls = [dvs.find_all('a', class_= "vsmall")[0]['href'] for dvs in divs]

    for name, url in zip(names, urls):
        new_matche = Upcoming_matches(name=name, url=url)
        db.session.add(new_matche)
        db.session.commit()
        
    print(scores)