from django.db import models

# Create your models here.
class Board(models.Model):
    '''
    Class for message boards.
    '''
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __repr__(self):
        cls = self.__class__.__name__
        return f"<{cls}: name={self.name!r} description={self.description!r}>"

    def __str__(self):
        return self.name
