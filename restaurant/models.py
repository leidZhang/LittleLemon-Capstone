from django.db import models

# Create your models here.
class Booking(models.Model): 
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255) 
    no_of_guests = models.IntegerField() 
    bookingDate = models.DateTimeField() 

    def __str__(self) -> str:
        return str(self.id) 

class Menu(models.Model): 
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    inventory = models.IntegerField() 

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'