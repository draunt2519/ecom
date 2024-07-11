from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    fullname=models.CharField(max_length=255,blank=True)
    phone=models.CharField(max_length=50,blank=True)
    address=models.CharField(max_length=255,blank=True)
    total=models.DecimalField(max_digits=10,decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    customer=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return self.fullname +"  ที่อยู่ : "+self.address+ "    เบอร์โทร : "+self.phone +" รวมราคา = "+str(self.total) +" บาท "+"วันที่สั่งซื้อ : "+str(self.created)
    
class OrderDetail(models.Model):
    product=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    def __str__(self):
        return self.product +"  ราคา : "+str(self.price)+ " จำนวนทั้งหมด :"+str(self.quantity) 
        
    def sub_total(self):
        return self.price * self.quantity