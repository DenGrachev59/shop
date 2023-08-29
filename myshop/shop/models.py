from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Категория")
    slug = models.SlugField(max_length=200, unique=True)
    desc = models.TextField(**NULLABLE, verbose_name='Описание')

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']),
        ]
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=200, verbose_name='Имя')
    image = models.ImageField(upload_to='products/%Y/%m/%d', **NULLABLE, verbose_name='Фотография')
    slug = models.SlugField(max_length=200)
    desc = models.TextField(**NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created'])
        ]

        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return  f'{self.name} ({self.category})'


