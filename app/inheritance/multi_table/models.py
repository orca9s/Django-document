from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f'[{self.pk}] place({self.name})'

    class Meta:
        ordering = ['name']


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'[{self.pk}] Restaurant'


class Supplier(Place):
    # place_ptr = models.OneToOneField(Place)
    customers = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='supplier_by_customer',
    )

    # 특정 Place인 p1이 있을 때
    # Supplier.objects.filter(customer=p1)
    # Supplier.objects.filter(place_ptr=p1)

    # p1이 역방향 Manager를 사용할 때
    # related_name 안겹침
    # p1.supplier_set   <-MTO
    # p1.supplier       <-OTO (역방향 매니저가 존재하지 않음)

    # p1이 역방향 Query를 사용할 때
    #   related_name 및 related_query_name에 아무것도 지정하지 않았을때
    #   related_query_name의 기본값:
    #       클래스명의 lowercase
    #           -> supplier(겹침)
    #   겹치지 않도록 related_name 또는 related_query_name을 지정해준다.
