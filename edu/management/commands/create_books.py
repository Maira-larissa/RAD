from django.core.management.base import BaseCommand
from faker import Faker
from ...models import Livro, Editora, Autor
import random

class Command(BaseCommand):
    help = 'Cria livros fictícios na base de dados'

    def handle(self, *args, **options):
        fake = Faker('pt_BR')

        # Criando algumas editoras fictícias para associar aos livros
        editoras = [Editora.objects.create(nome=fake.unique.company()) for _ in range(10)]
        
        # Criando autores fictícios
        autores = [Autor.objects.create(nome=fake.name()) for _ in range(10)]

        for _ in range(100):  
            editora = random.choice(editoras) 
            autor = random.choice(autores) 

            livro = Livro.objects.create(
                isbn=fake.isbn13(), 
                titulo=fake.sentence(nb_words=4),
                publicacao=fake.date_this_century(), 
                preco=random.uniform(20.0, 150.0),
                estoque=random.randint(1, 100), 
                editora=editora  
            )

            livro.autores.add(autor)

        self.stdout.write(self.style.SUCCESS('100 livros foram criados com sucesso!'))