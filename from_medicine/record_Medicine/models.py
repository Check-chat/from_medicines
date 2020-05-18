from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    expirationDate = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}{}{}".format(self.category, self.name, self.purchase_date)


class Record(models.Model):
    name = models.ForeignKey(Product,on_delete=models.CASCADE)
    dosage = models.IntegerField()
    takingDate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{}{}".format(self.dosage, self.takingDate)