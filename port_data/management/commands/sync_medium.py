from django.core.management.base import BaseCommand
from port_data.models import Article
from port_data.utils import recuperer_articles_medium
import os
from dotenv import load_dotenv
load_dotenv()

class Command(BaseCommand):
    help = "Synchroniser les articles Medium avec la base de données"

    def handle(self, *args, **kwargs):
        # nom utlisateur medium
        USER_ID = os.getenv('USER_ID')
        articles = recuperer_articles_medium(USER_ID)

        if not articles:
            self.stdout.write(self.style.WARNING('Aucun article récuperé !'))
            return
        
        for article_data in articles:
            print(article_data)
            Article.objects.update_or_create(
                title = article_data['title'],
                defaults={
                    'content': article_data['content'],
                    'date_published': article_data["date_published"],
                    "categorie": article_data['categorie'],
                    'author_articles': article_data['author_articles']
                }
            )
        self.stdout.write(self.style.SUCCESS('Articles synchronisés avec succès! '))