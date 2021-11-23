from django.db import models

class Car(models.Model):
    brand_name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    year_type = models.IntegerField()
    trim_id = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)

    class Meta:
        db_table = "cars"