import urllib.request
import json
from typing import List


def get_articles(api_url: str) -> List[dict]:
    response = urllib.request.urlopen(api_url)
    response = response.read().decode()
    response = json.loads(response)
    articles = response['results']
    return articles

def _generate_doc(article: dict) -> dict:
    newArticle = {}
    newArticle['id'] = article['id']
    newArticle['name'] = article['name']
    newArticle['url'] = article['url']
    newArticle['status'] = article['status']
    newArticle['img_url'] = article['img_url'] or article['image_url']
    newArticle['net'] = article['net']
    newArticle['pad'] = article['pad']['name']
    newArticle['pad_url'] = article['pad']['map_url']
    newArticle['send'] = {}
    newArticle['send']['discord'] = False
    newArticle['send']['twitter'] = False
    return newArticle

