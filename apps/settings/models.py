from django.db import models

# Create your models here.
class ADS(models.Model):
    top_ads = models.ImageField(
        'Фото верхней рекламы',
        upload_to='ads/'
    )
    top_ads_link = models.URLField(
        'Ссылка верхней рекламы'
    )
    cat_ads = models.ImageField(
        'Фото рекламы в меню',
        upload_to='ads/'
    )
    cat_ads_link = models.URLField(
        'Ссылка рекламы в меню'
    )

    def __str__(self) -> str:
        return f"Реклама {self.id}"
    
    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Реклама'