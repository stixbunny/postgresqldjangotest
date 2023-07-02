from django.db import models

class Film(models.Model):
    G_ACTION = "ACC"
    G_COMEDY = "COM"
    G_DOC = "DOC"
    G_SCIFI = "SCI"
    G_HORROR = "HORR"
    G_ANIMATED = "ANIM"
    G_DRAMA = "DRAM"
    GENRE_CHOICES = [
        (G_ACTION, "Acción"),
        (G_COMEDY, "Comedia"),
        (G_DOC, "Documental"),
        (G_SCIFI, "Ciencia Ficción"),
        (G_HORROR, "Horror"),
        (G_ANIMATED, "Animada"),
        (G_DRAMA, "Drama")
    ]
    name = models.CharField("Nombre", max_length=50)
    release_date = models.DateField("Fecha de estreno", )
    genre = models.CharField("Género", max_length=5, choices=GENRE_CHOICES, blank=True)
    RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    rating = models.SmallIntegerField("Calificación", choices=RATING_CHOICES, blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.name} ({self.release_date.year})"
