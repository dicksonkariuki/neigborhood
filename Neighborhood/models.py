from django.db import models
from django.contrib.auth.models import User

class Neighborhood(models.Model):
    hood_name = models.CharField(max_length=100)
    hood_location = models.CharField(max_length=100)
    occupants = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.hood_location}"

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def search_neighbourhood(cls,hood_id):
        hood = cls.objects.get(id=hood_id)
        return hood 

    def update_hood(self,name):
        self.hood_name = name
        self.save()
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='prof_pics/',blank=True)
    user_location = models.CharField(max_length=200)
    prof_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    hood_id = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.prof_user}"

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
class Business(models.Model):
    business_name = models.CharField(max_length=200)
    business_email = models.EmailField()
    business_owner = models.ForeignKey(User,on_delete=models.CASCADE)
    business_hood_id = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.business_name}"

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()
    
    @classmethod
    def search_business_by_title(cls,search_term):
        post = cls.objects.filter(business_name__icontains=search_term)
        return post    
    @classmethod
    def search_business(cls,biz_id):
        business = cls.objects.get(id=biz_id)
        return business 
class Post(models.Model):
    post_picture = models.ImageField(upload_to='posts/',blank=True)
    post_name = models.CharField(max_length=200)
    post_description = models.TextField()
    date_posted = models.DateField(auto_now=True)
    post_owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    hood_post = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.post_name}"

    class Meta:
        ordering = ['-id']

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
class ContactInfo(models.Model):
    health_department = models.CharField(max_length=200)
    police_department = models.CharField(max_length=200)
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.health_department}"

    def save_contact(self):
        self.save()

    def delete_contact(self):
        self.delete()   
    
