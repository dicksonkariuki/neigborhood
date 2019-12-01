from django.db import models

class Neighborhood(models.Model):
    hood_name = models.CharField(max_length=100)
    hood_location = models.CharField(max_length=100)
    occupants = models.IntegerField(default=0)

    def __str__(self):
        return self.hood_name

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
        return self.prof_user

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
