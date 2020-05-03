from django.db import models
from datetime import date

class InitialChat(models.Model):
    person_id=models.CharField(max_length=255)
    stage=models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.person_id)

class RegisteredPerson(models.Model):
    person_id = models.CharField(max_length=255)
    fb_name = models.CharField(max_length=255)
    fb_gender = models.CharField(max_length=255)
    fb_url=models.CharField(max_length=255)
    mask_avail=models.CharField(max_length=10)
    mask_price = models.CharField(max_length=255)
    sanitizer_avail = models.CharField(max_length=10)
    sanitizer_price = models.CharField(max_length=255)
    shop_name = models.CharField(max_length=255)
    locality = models.TextField()
    pincode = models.CharField(max_length=255)
    contact = models.CharField(max_length=12,default="not provided")
    registration_date = models.DateField(default=date.today)
    registration_time = models.TimeField(auto_now_add=True)

class DailyUpdate(models.Model):
    person = models.ForeignKey(RegisteredPerson,on_delete=models.CASCADE,related_name='daily')
    shop_open = models.CharField(max_length=10)
    mask_avail = models.CharField(max_length=10)
    sanitizer_avail = models.CharField(max_length=10)
    update_date = models.DateField(default=date.today)
    update_time = models.TimeField(auto_now_add=True)

class Web_Registration(models.Model):
    first_name = models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    contact_name=models.CharField(max_length=255)
    shop_owner = models.CharField(max_length=255)
    mask_avail=models.CharField(max_length=255)
    mask_price = models.CharField(max_length=255)
    sanitizer_avail = models.CharField(max_length=255)
    sanitizer_price = models.CharField(max_length=255)
    shop_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    pincode=models.CharField(max_length=255)
    update_date = models.DateField(default=date.today)
    update_time = models.TimeField(auto_now_add=True)


