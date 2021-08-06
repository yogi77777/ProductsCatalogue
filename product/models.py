from django.db import models
from users.models import CustomUser
import uuid
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=500)
    img = models.FileField(upload_to="products/",blank=True, null=True)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)

    def __str__(self):
        return str(self.id)+"  "+str(self.title)

class Order(models.Model):
    order_id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)

    def __str__(self):
        return str(self.order_id)
    

    