from django.db import models


class Car(models.Model):
    manufacturer = models.ForeignKey(
        # 문자열로 바꿔주면 car클래스를 위로 써도 된다. 파이썬에서는 안되고 장고에서 제공하는 기능이다.
        'Manufacturer',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ForeignkeyUser(models.Model):
    name = models.CharField(max_length=50)
    instructor = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='students',
        blank=True,
        null=True,
    )
