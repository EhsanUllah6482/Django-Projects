from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False,db_index=True)

    # def save(self, *args, **kwargs):
    #     self.slug=slugify(self.title)
        
    #     super().save(*args,**kwargs)


    def __str__(self):
        return f"{self.title} - {self.rating}"
