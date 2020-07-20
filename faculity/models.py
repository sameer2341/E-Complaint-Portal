from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Faculity_info(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    user_name = models.CharField(max_length=70,null=True)
    password = models.CharField(max_length=32)
    email = models.EmailField( max_length=254)
    designation = models.CharField(max_length=32)
    department = models.CharField(max_length=50,null=True)
    class Meta:
        ordering = ['pk']
    def __str__(self):
        return '{} {}'.format(self.user,self.email)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	
	if created:
		Faculity_info.objects.create(user=instance)
		print('Profile created!')
class Rejcomplaint(models.Model):
    id = models.IntegerField(primary_key=True)
    complain_about = models.CharField(max_length=50)
    reason=models.TextField()
    complain_too = models.CharField(max_length=50)
    complain = models.TextField()

    class Meta:
        ordering =  ['-id']
    def __str__(self):
        return '{} {} '.format(self.id,self.complain_about)
class solcomplaint(models.Model):
    id = models.IntegerField(primary_key=True)
    complain_about = models.CharField(max_length=50)
    solution=models.TextField()
    complain_too = models.CharField(max_length=50)
    complain = models.TextField()

    class Meta:
        ordering =  ['-id']
    def __str__(self):
        return '{} {} '.format(self.id,self.complain_about)
class Acomplaint(models.Model):
    id = models.IntegerField(primary_key=True)
    complain_about = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    complain_too = models.CharField(max_length=50)
    complain = models.TextField()
    send_to=models.CharField(max_length=50)
    forward=models.CharField(max_length=50)
    user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    class Meta:
        ordering =  ['-id']
    def __str__(self):
        return '{}  '.format(self.id)
class dcomplaint(models.Model):
    id = models.IntegerField(primary_key=True)
    complain_about = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    complain_too = models.CharField(max_length=50)
    complain = models.TextField()
    send_to=models.CharField(max_length=50)
    forward=models.CharField(max_length=50)
    user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    class Meta:
        ordering =  ['-id']
    def __str__(self):
        return '{}  '.format(self.id)
class Appcomplaint(models.Model):
    id = models.IntegerField(primary_key=True)
    complain_about = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    complain_too = models.CharField(max_length=50)
    complain = models.TextField()
    user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    class Meta:
        ordering =  ['-id']
    def __str__(self):
        return '{}  '.format(self.id)
class ComplaintUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    complain_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc