from django.db import models

# Create your models here.
GENRE_CHOICES = (
    ("R", "Рок"),
    ("E", "Электроника"),
    ("P", "Поп"),
    ("C", "Классика"),
    ("O", "Саундтреки"),
)


class CD(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    artist = models.CharField(max_length=40)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    # price = models.DecimalField(max_digits=10000, decimal_places=10)
    # comment = models.TextField(null=True, blank=True)
    # name = models.CharField(max_length=100)
    # email = models.EmailField()

    def __repr__(self):
        return "Вот я такой кросавчик"