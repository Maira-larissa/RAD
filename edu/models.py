from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Editora(models.Model):
    nome = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=200)
    publicacao = models.DateField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()

    editora = models.ForeignKey(
        Editora,
        on_delete=models.CASCADE,
        related_name='livros'
    )

    autores = models.ManyToManyField(
        Autor,
        through='Publica',
        related_name='livros'
    )

    def __str__(self):
        return self.titulo


class Publica(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('livro', 'autor')
        # alternativa moderna:
        # constraints = [
        #     models.UniqueConstraint(fields=['livro', 'autor'], name='unique_livro_autor')
        # ]

    def __str__(self):
        return f"{self.livro} - {self.autor}"