import random
from django.core.management.base import BaseCommand

from django.contrib.admin.utils import flatten
from django_seed import Seed

from favs import models as favs_models
from users import models as users_models
from books import models as books_models
from movies import models as movies_models


NAME = "favs"

class Command(BaseCommand):  # 노트 9 참조
    help = f"{NAME} 더미데이터 생성"

    def get_clean_user(self):
        favs_user_list = []
        for favs_object in favs_models.FavList.objects.all():
            favs_user_list.append(favs_object.created_by.username)             
        non_fav_user = []
        for user in users_models.User.objects.all():
            if user.username in favs_user_list:
                continue
            non_fav_user.append(user)        
        random.shuffle(non_fav_user)
        
        return non_fav_user.pop()

    def add_arguments(self, parser):
        parser.add_argument(
            '--total',
            default=1,
            type=int,
            help=f'{NAME}을/를 number 만큼 생성합니다.',
        )

    def handle(self, *args, **options):
        number = options.get("total")
        seeder = Seed.seeder()

       
        all_books = books_models.Book.objects.all()
        all_movies = movies_models.Movie.objects.all()           
        
        seeder.add_entity(
            favs_models.FavList,
            number,
            {
                "created_by": lambda x:self.get_clean_user(),
            }
        )

        created_favs = seeder.execute()          
        created_favs_pk_clean = flatten(list(created_favs.values()))          

        for pk in created_favs_pk_clean:
            pk_favs = favs_models.FavList.objects.get(pk=pk)               
            for a_b in all_books: 
                magic_number = random.randint(0, 15)
                if magic_number % 3 == 0:
                    pk_favs.books.add(a_b) 
                     
            for a_m in all_movies: 
                magic_number = random.randint(0, 15)
                if magic_number % 3 == 0:
                    pk_favs.movies.add(a_m)  

        self.stdout.write(
            self.style.SUCCESS(f"{number} {NAME} created!!")
        )
