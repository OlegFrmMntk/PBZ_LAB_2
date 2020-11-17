from django.db import models


# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100)
    type_of_organization = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'


class ExhibitionHall(models.Model):
    name = models.CharField(max_length=100)
    area = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'


class Artist(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    biography = models.CharField(max_length=1000)
    education = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name} ({self.id})'


class Artwork(models.Model):
    name = models.CharField(max_length=100)
    execution = models.CharField(max_length=100)
    date_of_create = models.DateField()
    size = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'


class Exhibition(models.Model):
    name = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    exhibition_hall = models.ForeignKey(ExhibitionHall, on_delete=models.PROTECT)
    artwork = models.ManyToManyField(Artwork, null=True)

    def __str__(self):
        return f'{self.name} ({self.id})'

