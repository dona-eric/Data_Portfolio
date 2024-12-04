import  requests
from datetime import datetime



## ce fichier permet de requeter à travers l'api de medium pour recuperer tous les articles

def recuperer_articles_medium(USER_ID):
    # api de medium
    url = f"https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@{USER_ID}"
    response = requests.get(url)
    print(response.status_code, response.content)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('item', [])

        return [
            {
                'title': article['title'],
                'content': article['content'],
                'categorie': article['categorie'],
                'date_published': datetime.strptime(article['date_published'], "%Y-%m-%d %H:%M:%S"),
                'author_articles': article['author_articles']
            }
            for article in articles
        ]
    else:
        return []