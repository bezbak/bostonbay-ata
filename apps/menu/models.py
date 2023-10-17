from django.db import models
from slugify import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(
        verbose_name='Имя категории',
        max_length=255
    )
    category_image = models.ImageField(
        'Фото категории',
        upload_to='images/'
    )
    slug = models.SlugField(
        unique=True,
        auto_created=True,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = self.slug
        else:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)  

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(
        'Название блюда',
        max_length=255
    )
    image = models.ImageField(
        'Фотография блюда',
        upload_to='images/'
    )
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    price = models.CharField(
        'Цена',
        max_length=50
    )

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'