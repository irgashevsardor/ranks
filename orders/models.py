from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # идентификатор price для получения стоимости товара (новый метод stripe для работы с платежами)
    price = models.FloatField()

    def __str__(self):
        return self.name
