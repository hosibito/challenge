import random

from django.core.management.base import BaseCommand
from django_seed import Seed

from categories import models as categories_models


NAME = "categories"


class Command(BaseCommand):  # 노트 9 참조
    help = f"{NAME} 더미데이터 생성"

    def add_arguments(self, parser):
        parser.add_argument(
            '--total',
            default=1,
            type=int,
            help=f'{NAME}을/를 total 만큼 생성합니다.',
        )

    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()     
        seeder.add_entity(
            categories_models.Category,
            total,
            {
                "name": lambda x: seeder.faker.sentence(),
                "kind": lambda x: random.choice(["book","movie","both"]),
            }
        )
        seeder.execute()              

        self.stdout.write(
            self.style.SUCCESS(f"{total} {NAME} created!!")
        )
