from django.db import models

# Create your models here.
class Donation(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    payment_id = models.CharField(max_length=50,blank=True,null=True)
    payment_captured = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ": " + str(self.amount)
    