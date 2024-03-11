from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    type = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(Person, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.type} - {self.owner.name}"


class Rent(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    client = models.ForeignKey(Person, on_delete=models.RESTRICT)

    """
    def __str__(self):
        return f"Rent ID: {self.id} - Car: {self.car.type} - Client: {self.client.name}"
    """