import random

from django.core.management.base import BaseCommand
from django_seed import Seed

from people import models as people_models


NAME = "people"


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
            people_models.Person,
            total,
            {
                "name": lambda x: seeder.faker.name(),
                "kind": lambda x: random.choice(["actor","director","writer"]),
            }
        )
        seeder.execute()              

        self.stdout.write(
            self.style.SUCCESS(f"{total} {NAME} created!!")
        )
