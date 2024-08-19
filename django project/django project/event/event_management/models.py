from django.db import models

class event(models.Model):
    img=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    descr=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class booking(models.Model):
    cus_name=models.CharField(max_length=55)
    cus_ph=models.CharField(max_length=55)
    name=models.ForeignKey(event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booking_on=models.DateField(auto_now=True)




